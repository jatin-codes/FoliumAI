# coding=utf-8
import os
cwd = os.getcwd()
import train_network, predict
import os
from time import time
import argparse
import pandas as pd
import multiprocessing
from time import time
import numpy as np
from collections import namedtuple
import gensim as gs
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
import os
import sys
import warnings
from random import shuffle
from sklearn.metrics.pairwise import cosine_similarity
from typing import Dict, List, Type
import matplotlib.pyplot as plt
import logging
from ast import literal_eval
import settings

def train_tags(labelled_data_path, unlabelled_data_path, random_state = 42, epochs = 10):

    PATH_TO_DATA = labelled_data_path

    tags_to_remove = ['use/modification of sap content']

    tags_to_merge = {
        'termination/suspension': 'changes to service',
        'consent': 'general requirements',
        'publicity': 'data security standards',
        'informed consent': 'privacy/data protection',
        'technical requirements': 'general requirements'
    }

    loader = LabeledData(os.path.realpath(os.path.join(os.getcwd(), PATH_TO_DATA)))

    loader.extract_excel()

    loader.add_infrequent(threshold=10)

    loader.add_manual(tags_to_remove=tags_to_remove)

    loader.remove_tags()

    loader.manual_remove()

    loader.merge_tags(mapper=tags_to_merge)

    raw_unlab = pd.read_excel(unlabelled_data_path)

    len_thres = 20

    col = 'content'  # use old paragraphs. also works on new_paragraphs column

    data_unlab = raw_unlab[raw_unlab[col].astype(str).map(lambda x: x.split()).str.len() > len_thres].copy()
    data_unlab.reset_index(drop=True, inplace=True)

    data_unlabeled = data_unlab.copy()  # only tag 200 for demo purpose

    data_unlabeled['text'] = data_unlabeled[col]  # old paragraphs
    data_unlabeled['tags'] = data_unlabeled.apply(lambda x: [], axis=1)

    print('Predicting tags ...')
    data_labeled = loader.data
    tags = loader.tags_to_keep
    tags_file = open("tags_old.txt", "w", encoding='utf-8')
    for tag in tags:
        tags_file.write(tag+'\n\n')
    #print(data_labeled.shape)
    #print(data_unlabeled.shape)
    #exit(0)
    tagging_unlab = TaggingSSL(data_labeled, tags, random_state,  data_unlabeled)
    tagging_unlab.set_stopwords()  # add customized stopwords here if needed

    tagging_unlab.set_hyperparams(min_count=1)  # using defaults

    tagging_unlab.run(epochs)





def predict_tags(input_text):
    name = 'tagging_model'

    #model = Doc2Vec.load(os.path.join(os.getcwd(),'server', 'ml', 'ALRA', 'models', 'doc2vec_models','tagging_model'))
    model = Doc2Vec.load('/var/www/WASP/WASP/src/server/ml/ALRA/models/doc2vec_models/tagging_model')
    input_tags = []
    df_test_dict = {
        'tags_true': [input_tags],
        'text': [input_text]
    }
    df_test = pd.DataFrame(df_test_dict)

    # df_train0 = pd.read_excel(os.path.join(os.getcwd(),'server', 'ml', 'ALRA', 'data', 'excel_files', 'labelled_new.xlsx'))
    df_train0 = pd.read_excel('/var/www/WASP/WASP/src/server/ml/ALRA/data/excel_files/labelled_new.xlsx')
    tags_list = df_train0['tags_ssl']
    tags_list_new = []
    for t in tags_list:
        tags = literal_eval(t)
        tags_list_new.append(tags)
    df_train_dict = {
        'tags_ssl':tags_list_new,
        'text': df_train0['text']
    }
    df_train = pd.DataFrame(df_train_dict)
    tagging = TaggingSSL(random_state=42)
    tagging.set_stopwords()
    tagging.set_hyperparams()
    result = tagging.predict_tags(df_train,df_test,model)
    print(result['tags_pred'][0])
    return result['tags_pred'][0]

#def predict_priority_statesments(statesments, priorities):

def train_similarity(labelled_data_path, unlabelled_data_path, changes_data_path,lr = 0.025, vector_size=50,epochs=20, save_models=1):
    lab, unlab, combined, changes = cs.run_data_preprocess_excel(labelled_tos=labelled_data_path,
                                                                 unlabelled_tos=unlabelled_data_path,
                                                                 changes_tos=changes_data_path)
    models = dt.train_doc2vec(combined, lr, vector_size, epochs, save_models)

def predict_similarity(old_paragraph, new_paragraph, only_insert = 0, only_delete = 0):
    olds = [old_paragraph]
    news = [new_paragraph]
    only_ins = [only_insert]
    only_del = [only_delete]
    changes = {
        'old_paragraphs': olds,
        'new_paragraphs': news,
        'only_inserts': only_ins,
        'only_deletes': only_del
    }
    #path = os.path.join(os.getcwd(),'server', 'ml', 'ALRA', 'models', 'doc2vec_models')
    path = '/var/www/WASP/WASP/src/server/ml/ALRA/models/doc2vec_models'
    changes_df = pd.DataFrame(changes)
    dt.test_doc2vec_pre_trained(changes_df= changes_df, doc2vec_folder_path=path)
    concat_columns = [col for col in changes_df.columns if 'concat' in col.split('_')[0]]
    changes_df['semantic_score'] = changes_df[concat_columns].mean(axis=1)
   # changes__df.to_csv('./changes_2.csv')
    scores = changes_df['semantic_score']
    fn = ((10 ** 5) - (10 ** scores[0])) / 200
    if 5 - fn < 0:
        return 0

    # min -203.08730851914152
    # max -3616.066426303878
    return 5 - fn



#All the urls and other parameters should be imported from settings.py The documentation should be in readme
'''

if __name__ == "__main__":
    #predict_tags('Box reserves the right to change its prices at any time, however, if we have offered a specific duration and Fee for your use of the Service, we agree that the Fee will remain in force for that duration.  After the offer period ends, your use of the Service will be charged at the then-current Fee(s).  If you don\'t agree to these changes, you must stop using the Service and cancel via email to cancel@box.com (with cancellation confirmation from a Box representative).  If you cancel, your Service ends at the end of your current Service period or payment period, and no refunds for previously paid services will be issued. ')
    #train_tags(os.path.join('data', 'excel_files', 'labelled.xlsx'), os.path.join('data', 'excel_files', 'unlabelled.xlsx'))
    #predict_similarity("I certainly eat", "You do not eat")
    #train_similarity(os.path.join('data', 'excel_files', 'labelled.xlsx'), os.path.join('data', 'excel_files', 'unlabelled.xlsx'), os.path.join('data', 'excel_files', 'diff_file.xlsx'))
'''

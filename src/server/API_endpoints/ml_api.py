'''
    @Author: Kai Sackville-Hii && Turash
    @Company: SAP - R&I in GTLC

    @Description
        This class handles the machine learning endpoints.
'''

from flask import request
from flask_restful import Resource
from server.ml.ALRA.interface import *

class ML_api(Resource):

    def __init__(self,**kwargs):
        print('init ML_api')

    def options(self):
        return({
            "allowed_methods": ['post'],
        })

    """
    @api {post} /api/ml Query ALRA 
    @apiGroup Machine Learning
    @apiVersion 2.0.0
    @apiDescription This endpoint will Query the ALRA model based on the action value posted. If action is predict tags, 
                    then the payload must be a string which ALRA will predict the tags for. If action is predict similarity,
                    then the payload must be an array containing the two strings to compare.
    
    @apiParam {String} action Command for ALRA to execute ('predict tags', or 'predict similarity')
    @apiParam {String/Array} payload Inputs for ALRA to use.
    """
    def post(self):
        # try:
        args = request.get_json()

        if args['action'] == 'predict tags':
            input = args['payload']
            resp = predict_tags(input)
            print("predicting tags")

        elif args['action'] == 'predict similarity':
            docA = args['payload'][0]
            docB = args['payload'][1]
            resp = predict_similarity(docA, docB)

            if round(resp, 5) == 5.0:
                resp = 5.0
            print("predicting similarity")
        return resp
        #
        # except Exception as e:
        #     return({
        #         'code': 400,
        #         'messages': str(e)
        #     })

import json
from bs4 import BeautifulSoup
import urllib.request as urllib2

from flask import request
from flask_restful import Resource



class Info_api(Resource):

    def __init__(self, **kwargs):
        print('init Info_api')

    def options(self):
        return ({
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

        if args['action'] == 'get info':
            input = args['payload']
            resp = get_data(input)
            print("getting info")

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


'''
Common Name: Japanese maple 
Type: Tree
Family: Sapindaceae
Native Range: Korea, Japan
Zone: 5 to 8
Height: 10.00 to 25.00 feet
Spread: 10.00 to 25.00 feet
Bloom Time: April
Bloom Description: Reddish-purple
Sun: Full sun to part shade
Water: Medium
Maintenance: Low
Flower: Insignificant
Leaf: Good Fall
Tolerate: Rabbit, Black Walnut

'''
def get_data(name):
    lookup_table = {}
    lookup_table["Acer Palmatum"] = "b974"
    lookup_table["Aesculus Californica"] = "http://www.missouribotanicalgarden.org/PlantFinder/PlantFinderDetails.aspx?taxonid=281051&isprofile=0&"
    if(name in lookup_table.keys()):
        kempercode = lookup_table[name]
    else:
        return {}
    keys =["name","type", "family", "native", "zone", "hight", "spread", "bloom", "color", "sun", "water", "maintain", "culture", "note", "problem", "garden"]
    fields = []
    if(len(kempercode)<=4):
        quote_page = 'http://www.missouribotanicalgarden.org/PlantFinder/PlantFinderDetails.aspx?kempercode='+kempercode
    else:
        quote_page = kempercode
    page = urllib2.urlopen(quote_page)
    soup = BeautifulSoup(page, 'html.parser')
    name = soup.find('div', attrs={'id': 'MainContentPlaceHolder_CommonNameRow'})
    if(name is not None):
        fields.append(name.text.strip())
    else:
        fields.append("Name: Not available")
    name = soup.find('div', attrs={'id': 'MainContentPlaceHolder_TypeRow'})
    if (name is not None):
        fields.append(name.text.strip())
    else:
        fields.append("Type: Not available")
    name = soup.find('div', attrs={'id': 'MainContentPlaceHolder_FamilyRow'})
    if (name is not None):
        fields.append(name.text.strip())
    else:
        fields.append("Family: Not available")
    name = soup.find('div', attrs={'id': 'MainContentPlaceHolder_NativeRangeRow'})
    if (name is not None):
        fields.append(name.text.strip())
    else:
        fields.append("Native: Not available")
    name = soup.find('div', attrs={'id': 'MainContentPlaceHolder_ZoneRow'})
    if (name is not None):
        fields.append(name.text.strip())
    else:
        fields.append("Zone: Not available")
    name = soup.find('div', attrs={'id': 'MainContentPlaceHolder_HeightRow'})
    if (name is not None):
        fields.append(name.text.strip())
    else:
        fields.append("Height: Not available")
    name = soup.find('div', attrs={'id': 'MainContentPlaceHolder_SpreadRow'})
    if (name is not None):
        fields.append(name.text.strip())
    else:
        fields.append("Spread: Not available")
    name = soup.find('div', attrs={'id': 'MainContentPlaceHolder_BloomTimeRow'})
    if (name is not None):
        fields.append(name.text.strip())
    else:
        fields.append("Bloom Time: Not available")
    name = soup.find('div', attrs={'id': 'MainContentPlaceHolder_ColorTextRow'})
    if (name is not None):
        fields.append(name.text.strip())
    else:
        fields.append("Bloom Color: Not available")
    name = soup.find('div', attrs={'id': 'MainContentPlaceHolder_SunRow'})
    if (name is not None):
        fields.append(name.text.strip())
    else:
        fields.append("Preferred Sunlight: Not available")
    name = soup.find('div', attrs={'id': 'MainContentPlaceHolder_WaterRow'})
    if (name is not None):
        fields.append(name.text.strip())
    else:
        fields.append("Water Required: Not available")
    name = soup.find('div', attrs={'id': 'MainContentPlaceHolder_MaintenanceRow'})
    if (name is not None):
        fields.append(name.text.strip())
    else:
        fields.append("Maintenance: Not available")
    name = soup.find('div', attrs={'id': 'MainContentPlaceHolder_CultureRow'})
    if (name is not None):
        fields.append(name.text.strip())
    else:
        fields.append("Culture: Not available")
    name = soup.find('div', attrs={'id': 'MainContentPlaceHolder_NoteworthyRow'})
    if (name is not None):
        fields.append(name.text.strip())
    else:
        fields.append("Noteworthy Feature: Not available")
    name = soup.find('div', attrs={'id': 'MainContentPlaceHolder_ProblemsRow'})
    if (name is not None):
        fields.append(name.text.strip())
    else:
        fields.append("Problems: Not available")
    name = soup.find('div', attrs={'id': 'MainContentPlaceHolder_GardenUseRow'})
    if (name is not None):
        fields.append(name.text.strip())
    else:
        fields.append("Garden: Not available")
    output_dict = {}
    for i in range(len(keys)):
        print(str(fields[i]))
        output_dict[keys[i]]=fields[i]
    return json.dumps(output_dict)
if __name__ == "__main__":
    get_data("Aesculus Californica")
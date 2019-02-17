#from server.utils.RequestHandler import RequestHandler
from pymongo import MongoClient

def init(args):
    #global requestHandler
    global client

    global dev

    # Create MongoDB client to WASP db
    client = MongoClient('localhost', connect=False)


    # Create request handler object
    #requestHandler = RequestHandler()

    # Development flag
    if '-dev' in args:
        print('running App in development mode')
        dev = True
    else:
        dev = False

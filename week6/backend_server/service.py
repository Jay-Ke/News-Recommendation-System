'''Backend service'''
#import os
#import sys
#import json
#from bson.json_util import dumps
import operations

from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer # pylint: disable = wrong-import-order

#sys.path.append(os.path.join(os.path.dirname(__file__), 'utils'))

#import mongodb_client # pylint: disable=import-error, wrong-import-position

SERVER_HOST = 'localhost'
SERVER_PORT = 4040

def add(num1, num2):
    '''Test add function'''
    print('function being called')
    return num1 + num2


def get_one_news():
    '''Test get one news function'''
    print('getting one news')
    #news = mongodb_client.get_db()['news'].find_one()
    #return json.loads(dumps(news))
    return operations.get_one_news()



RPC_SERVER = SimpleJSONRPCServer((SERVER_HOST, SERVER_PORT))
RPC_SERVER.register_function(add, 'add')
RPC_SERVER.register_function(get_one_news, 'get_one_news')

print('starting rpc server on %s:%d' %(SERVER_HOST, SERVER_PORT))

RPC_SERVER.serve_forever()

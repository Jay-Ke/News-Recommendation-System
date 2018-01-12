'''Operation'''
import os
import sys
import json
from bson.json_util import dumps

sys.path.append(os.path.join(os.path.dirname(__file__), 'utils'))

import mongodb_client # pylint: disable=import-error, wrong-import-position

NEWS_TABLE_NAME="news"

def get_one_news():
    '''Test get one news function'''
    print('getting one news')
    news = mongodb_client.get_db()[NEWS_TABLE_NAME].find_one()
    return json.loads(dumps(news))


import datetime
import hashlib
import redis
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))

import news_api_client
from cloudAMQP_client import CloudAMQPClient

SLEEP_TIME_IN_SECONDS = 10
NEWS_TIME_OUT_IN_SECONDS = 3600 * 24 * 3

REDIS_HOST = 'localhost'
REDIS_PORT = 6379

SCRAPE_NEWS_TASK_QUEUE_URL = 'amqp://bbumfosv:GpUp2-3VQ9_qtP1FG_hQspRivnz3C8Ks@termite.rmq.cloudamqp.com/bbumfosv'
#SCRAPE_NEWS_TASK_QUEUE_URL ='amqp://uuumeniz:tz3uYZNY0UsHuw-v8HE4Y5jmoixN1sGI@termite.rmq.cloudamqp.com/uuumeniz'
SCRAPE_NEWS_TASK_QUEUE_NAME = 'scrape-news-task-queue' 

'''NEWS_SOURCES = [
    'bbc-news',
    'bbc-sport',
    'bloomberg',
    'cnn',
    'entertainment-weekly',
    'espn',
    'ign',
    'techcrunch',
    'the-new-york-times',
    'the-wall-street-journal',
    'the-washington-post'
]'''

NEWS_SOURCES = [
    'cnn'
]

redis_client = redis.StrictRedis(REDIS_HOST, REDIS_PORT)
cloudAMQP_client = CloudAMQPClient(SCRAPE_NEWS_TASK_QUEUE_URL, SCRAPE_NEWS_TASK_QUEUE_NAME)

while True:
    news_list=news_api_client.getNewsFromSource(NEWS_SOURCES)
    
    number_of_news=0

    for news in news_list:
        news_digest = hashlib.md5(news['title'].encode('utf-8')).hexdigest()

        if (redis_client.get(news_digest) is None):
            number_of_news+=1
            news['digest']=news_digest

            if (news['publishedAt'] is None):
                news['publishedAt'] = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
            
            redis_client.set(news_digest,'True')
            redis_client.expire(news_digest,NEWS_TIME_OUT_IN_SECONDS)
            cloudAMQP_client.sendMessage(news)
    print('Number of news %d' % number_of_news)

    cloudAMQP_client.sleep(SLEEP_TIME_IN_SECONDS)


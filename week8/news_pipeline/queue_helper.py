import os
import sys

# import common package in parent directory
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))

from cloudAMQP_client import CloudAMQPClient

SCRAPE_NEWS_TASK_QUEUE_URL = 'amqp://bbumfosv:GpUp2-3VQ9_qtP1FG_hQspRivnz3C8Ks@termite.rmq.cloudamqp.com/bbumfosv'
#SCRAPE_NEWS_TASK_QUEUE_URL ='amqp://qxvgsyko:As2dYa3bS8TNajsgb0nD1Zvc0VF1Oh7C@termite.rmq.cloudamqp.com/qxvgsyko'
SCRAPE_NEWS_TASK_QUEUE_NAME = 'scrape-news-task-queue'

DEDUPE_NEWS_TASK_QUEUE_URL = 'amqp://uuumeniz:tz3uYZNY0UsHuw-v8HE4Y5jmoixN1sGI@termite.rmq.cloudamqp.com/uuumeniz'
DEDUPE_NEWS_TASK_QUEUE_NAME = 'dedupe-news-task-queue'

def clearQueue(queue_url, queue_name):
    scrape_news_queue_client = CloudAMQPClient(queue_url, queue_name)

    num_of_messages = 0

    while True:
        if scrape_news_queue_client is not None:
            msg = scrape_news_queue_client.getMessage()
            if msg is None:
                print("Cleared %d messages." % num_of_messages)
                return
            num_of_messages += 1


if __name__ == "__main__":
    clearQueue(SCRAPE_NEWS_TASK_QUEUE_URL, SCRAPE_NEWS_TASK_QUEUE_NAME)
    clearQueue(DEDUPE_NEWS_TASK_QUEUE_URL, DEDUPE_NEWS_TASK_QUEUE_NAME)
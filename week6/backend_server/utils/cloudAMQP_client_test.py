from cloudAMQP_client import CloudAMQPClient

CLOUDAMQP_URL = "amqp://uuumeniz:tz3uYZNY0UsHuw-v8HE4Y5jmoixN1sGI@termite.rmq.cloudamqp.com/uuumeniz"
TEST_QUEUE_NAME = "test"

def test_basic():
    client = CloudAMQPClient(CLOUDAMQP_URL, TEST_QUEUE_NAME)

    sentMsg = {"test":"test"}
    client.sendMessage(sentMsg)
    receivedMsg = client.getMessage()

    assert sentMsg == receivedMsg
    print("test_basic passed!")

if __name__ == "__main__":
    test_basic()
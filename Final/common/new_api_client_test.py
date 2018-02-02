import news_api_client as client

def test():
    news=client.getNewsFromSource()
    print(news)
    assert len(news)>0
    print("test passed")

if __name__ == "__main__":
    test()
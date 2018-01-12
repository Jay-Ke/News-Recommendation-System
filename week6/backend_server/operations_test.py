import operations

def test():
    news = operations.get_one_news()
    assert news is not None
    print("test passed")

if __name__ == "__main__":
    test()

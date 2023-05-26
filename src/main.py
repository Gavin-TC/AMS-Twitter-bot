import csvretriever
import data
import tweeter

tweet = tweeter()
retriever = csvretriever()

def main():
    retriever.retrieve_csv()
    oldest = data.return_oldest_csv()
    latest = data.return_newest_csv()

def compare_dates():
    retriever.retrieve_csv()
    oldest = data.return_oldest_csv()
    latest = data.return_newest_csv()


if __name__ == '__main__':
    main()
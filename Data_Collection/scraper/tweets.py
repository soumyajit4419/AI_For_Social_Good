import snscrape.modules.twitter as sntwitter


def get_tweets(list_of_query, limit=1000):

    maxTweets = limit

    tweet_id = []
    tweet_date = []
    tweet_content = []

    for keyword in list_of_query:
        for i, tweet in enumerate(sntwitter.TwitterSearchScraper(keyword + ' since:2020-01-01 until:2021-02-15 lang:en').get_items()):
            if i >= maxTweets:
                break
            tweet_id.append(tweet.id)
            tweet_content.append(tweet.content)
            tweet_date.append(tweet.date)

    res_dict = {"id": tweet_id, "date": tweet_date, "text": tweet_content}
    return res_dict

import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    # result = tweets["content"].str.len()>15
    # result = tweets[result][["tweet_id"]]
    # return result
    mask = [len(text) > 15 for text in tweets["content"]]
    return tweets.loc[mask, ["tweet_id"]]
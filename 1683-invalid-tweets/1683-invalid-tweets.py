import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    result = tweets["content"].str.len()>15
    result = tweets[result][["tweet_id"]]
    return result
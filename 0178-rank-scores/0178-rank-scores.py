import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    scores['rank']=scores['score'].rank(method="dense",ascending=False).astype(int)
    result= scores.sort_values("score",ascending=False)
    return result[['score','rank']]
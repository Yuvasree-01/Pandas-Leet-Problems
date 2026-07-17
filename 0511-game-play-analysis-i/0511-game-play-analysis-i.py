import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    activity.sort_values(by="event_date",ascending=True,inplace=True)
    result=activity[["player_id","event_date"]].drop_duplicates(subset="player_id",keep="first")
    result.rename(columns={"event_date":"first_login"},inplace=True)
    return result
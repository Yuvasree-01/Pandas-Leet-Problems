import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    condition=(world['population']>=25000000) | (world['area']>=3000000)
    result = world[condition][["name","population","area"]]
    return result

from config import API_KEY
from polygon import RESTClient
import pandas as pd

client = RESTClient(API_KEY)

def get_data(ticker) -> pd.DataFrame:
    aggs = []

    for a in client.list_aggs(
        ticker=ticker,
        multiplier=1,
        timespan='day',
        from_='2021-06-01',
        to='2026-06-01',
        limit=50000
    ):
        aggs.append(a)

    df = pd.DataFrame(aggs)

    return df

spy_df = get_data('SPY')
spy_df.to_pickle("spy_data.pkl")

gld_df = get_data("GLD")
gld_df.to_pickle("gld_data.pkl")
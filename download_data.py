from config import API_KEY
from polygon import RESTClient
import pandas as pd

client = RESTClient(API_KEY)

def get_data(ticker: str, start_date: str = None, end_date: str = None) -> pd.DataFrame:
    aggs = []

    if not start_date:
        start_date = '2024-01-01'
    if not end_date:
        end_date = '2025-12-31'

    for a in client.list_aggs(
        ticker=ticker,
        multiplier=1,
        timespan='day',
        from_=start_date,
        to=end_date,
        limit=50000
    ):
        aggs.append(a)

    df = pd.DataFrame(aggs)

    return df

spy_df = get_data('SPY')
spy_df.to_pickle("spy_data.pkl")

gld_df = get_data("GLD")
gld_df.to_pickle("gld_data.pkl")
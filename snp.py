import os
import pandas as pd
import yfinance as yf

S_AND_P_URL = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'

def get_ticker_data(tickers: list):
    data = yf.download(
        tickers=tickers,
        interval='1d',
        group_by='ticker',
        threads=True,
    )

    data = data.T
    all_downloaded_tickers = list(set([idx[0] for idx in data.index]))

    for ticker in all_downloaded_tickers:
        df = data.loc[ticker, :].T.sort_index().dropna()
        df.to_csv(f'data/{ticker}.csv', index=True)
    return

def get_s_and_p_tickers() -> list:
    return pd.read_html(S_AND_P_URL)[0]['Symbol'].tolist()

if __name__ == '__main__':
    if not os.path.isdir('data'):
        os.mkdir('data')

    get_ticker_data(get_s_and_p_tickers())

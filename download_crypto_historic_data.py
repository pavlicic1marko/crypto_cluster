from datetime import datetime
import time
import json
import pandas as pd




def construct_download_urls(
        ticker_list,
        period1,
        period2,
        tick_interval='daily'
):
    """
	:period1 & period2: 'yyyy-mm-dd'
	:interval: {daily; weekly, monthly}
	"""

    def convert_to_seconds(period):
        datetime_value = datetime.strptime(period, '%Y-%m-%d')
        total_seconds = int(time.mktime(datetime_value.timetuple())) + 86400
        return total_seconds

    try:
        interval_reference = {'daily': '1d', 'weekly': '1wk', 'monthly': '1mo'}
        _interval = interval_reference.get(tick_interval)
        if _interval is None:
            print('interval code is incorrect')
            return
        p1 = convert_to_seconds(period1)
        p2 = convert_to_seconds(period2)
        dict_url_ticker={}
        for ticker in ticker_list:
            dict_url_ticker[ticker] = f'https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={p1}&period2={p2}&interval={_interval}&filter=history'
        download_data(dict_url_ticker)

    except Exception as e:
        print(e)
        return

def save_data_to_file(data, ticker_name:str):
    data.to_csv(ticker_name + '_Historical_Data1.csv')


def download_data(urls_dict):
    for key,value in urls_dict.items():
        df = pd.read_csv(value)
        df.set_index('Date', inplace=True)
        save_data_to_file(df,key)


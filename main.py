from download_crypto_historic_data import *
crypto_currency_to_download = ['BTC-USD', 'ETH-USD', 'BNB-USD', 'SOL-USD','USDC-USD','USDT-USD','XRP-USD','TON-USD','DOGE-USD','ADA-USD','TRX-USD','AVAX-USD','SHIB-USD','DOT-USD','LINK-USD','BCH-USD']
start_date = '2024-01-27'
end_date = '2024-03-27'
interval = 'daily'

get_historical_data(crypto_currency_to_download, start_date, end_date, interval)




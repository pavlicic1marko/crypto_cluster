from download_crypto_historic_data import *
crypto_currency_to_download = ['BTC-USD', 'ETH-USD', 'BNB-USD']
start_date = '2024-03-27'
end_date = '2024-04-27'
interval = 'daily'

construct_download_urls(crypto_currency_to_download, start_date, end_date, interval)




import requests
import datetime

#%% static data
url = 'https://api.sgx.com/securities/v1.1/charts/historic/security_type/code/ticker'

#%% get price from api
def get_price(ticker, security_type):
    ticker_url = url.replace('security_type',security_type).replace('ticker',ticker)
    response = requests.get(url=ticker_url).json()

    # 'lt' assumed to stand for last traded
    prices = {}
    for d in response['data']['historic']:
        date = d['trading_time'].split('_')[0]
        date = datetime.datetime.strptime(date, '%Y%m%d').date()
        prices[date] = d['lt']
    return(prices)

#%%
codes = {'retailbonds':['RMRB','V7AB','V7BB'], 'stocks':['D05','O39']}
prices = {}
for security_type, ticker_list in codes.items():
    for ticker in ticker_list:
        prices[ticker] = get_price(ticker, security_type)
import requests, configparser

getByCurrencyURL = 'https://www.nbrb.by/api/exrates/rates/{currency}?parammode=2'

def getDataByCurrency(currency):
    try:
        data = requests.get(getByCurrencyURL.replace('{currency}', currency))
        return data.json()
    except requests.exceptions.ConnectionError:
        print('Error: no internet connection')
        return None

config = configparser.ConfigParser()
config.read('config')

list = []
currency_alpha = (config["currency_alpha"]["value"])
list = currency_alpha.replace(' ','').split(',')

for value in list:
    data_json = getDataByCurrency(value)
    if data_json is not None:
        print(data_json['Cur_Abbreviation'], end=': ')
        print(data_json['Cur_OfficialRate'])



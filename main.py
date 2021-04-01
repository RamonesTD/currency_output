import requests, configparser

getByCurrencyURL = 'https://www.nbrb.by/api/exrates/rates/{currency}?parammode=2'

list = []

def getDataByCurrency(currency):
    try:
        data = requests.get(getByCurrencyURL.replace('{currency}', currency))
        return data.json()
    except requests.exceptions.ConnectionError:
        print('Error: no internet connection')
        return None

def setParamsFromConfig():
    config = configparser.ConfigParser()
    config.read('config')
    
    currency_alpha = (config["currency_alpha"]["value"])
    global list
    list = currency_alpha.replace(' ','').split(',')

setParamsFromConfig()
for value in list:
    data_json = getDataByCurrency(value)
    if data_json is not None:
        print(data_json['Cur_Abbreviation'], end=': ')
        print(data_json['Cur_OfficialRate'])



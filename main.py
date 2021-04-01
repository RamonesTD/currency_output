import requests, configparser

getByCurrencyURL = 'https://www.nbrb.by/api/exrates/rates/{currency}?parammode=2'

config = configparser.ConfigParser()
config.read('config')

list = []
currency_alpha = (config["currency_alpha"]["value"])
list = currency_alpha.replace(' ','').split(',')

try:

    for value in list:

        data = requests.get(getByCurrencyURL.replace('{currency}', value))
        data_json = data.json()

        print(data_json['Cur_Abbreviation'], end=': ')
        print(data_json['Cur_OfficialRate'])

except requests.exceptions.ConnectionError:
    print('Error: no internet connection')


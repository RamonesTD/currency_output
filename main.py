import requests, configparser

config = configparser.ConfigParser()
config.read('config')

list = []
currency_alpha = (config["currency_alpha"]["value"])
list = currency_alpha.replace(' ','').split(',')

try:

    for value in list:

        data = requests.get('https://www.nbrb.by/api/exrates/rates/' + value + '?parammode=2')
        data_json = data.json()

        print(data_json['Cur_Abbreviation'], end=': ')
        print(data_json['Cur_OfficialRate'])

except requests.exceptions.ConnectionError:
    print('Error: no internet connection')


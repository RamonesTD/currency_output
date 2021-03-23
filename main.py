import requests

def currency_support():
    values_cur_id = input('Введите Cur_ID валюты: ')
    return values_cur_id

#currency_id = currency_support()

data = requests.get('https://www.nbrb.by/api/exrates/rates/USD', data = {'parammode':'2'})
data_json = data.json()

print(data_json['Cur_OfficialRate'])
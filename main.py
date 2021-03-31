import requests

try:

    def currency_support():
        values_cur_alpha = input('Введите валюту: ')
        return values_cur_alpha

    currency_alpha = currency_support()

    data = requests.get('https://www.nbrb.by/api/exrates/rates/' + currency_alpha + '?parammode=2')
    data_json = data.json()

    print(data_json['Cur_Abbreviation'], end=': ')
    print(data_json['Cur_OfficialRate'])

except requests.exceptions.ConnectionError:
    print('Error: no internet connection')


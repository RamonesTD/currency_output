import requests

try:

    data = requests.get('https://www.nbrb.by/api/exrates/rates/145')
    data_json = data.json()

    print(data_json['Cur_Abbreviation'], end=': ')
    print(data_json['Cur_OfficialRate'])

except requests.exceptions.ConnectionError:
    print('Error: no internet connection')
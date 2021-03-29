import requests

data = requests.get('https://www.nbrb.by/api/exrates/rates/145')
data_json = data.json()

print(data_json['Cur_Abbreviation'], end=': ')
print(data_json['Cur_OfficialRate'])
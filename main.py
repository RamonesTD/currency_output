import requests, configparser, datetime, json

getByCurrencyAndDateURL = 'https://www.nbrb.by/api/exrates/rates/{currency}?parammode=2&ondate={date}'

list = []
compare = False
output = "block"

def getDataByCurrencyAndDate(currency, date):
    try:
        url = getByCurrencyAndDateURL.replace('{currency}', currency.lower()).replace('{date}', date.strftime("%Y-%m-%d"))
        data = requests.get(url)
        return data.json()
    except requests.exceptions.ConnectionError:
        print('Error: no internet connection')

def getAbbreviation(data):
    return data['Cur_Abbreviation']

def getRate(data):
    return data['Cur_OfficialRate']

def printData(data, end):
    global output
    if output == "block":
        print(getAbbreviation(data), end=': ')
        print(getRate(data), end='\n')
    elif output == "inline":
        print(getAbbreviation(data), end=': ')
        print(getRate(data), end=end+' ')

def setParamsFromConfig():
    config = configparser.ConfigParser()
    config.read('config')
    
    currency_alpha = (config["Global"]["currency"])
    global list
    list = currency_alpha.replace(' ','').split(',')
    global compare
    compare = config["Global"]["compare"].lower() == "true"
    global output
    output = config["Global"]["output"]

setParamsFromConfig()
for value in list:
    if compare:
        today = datetime.date.today()
        prewDay = datetime.date.today() - datetime.timedelta(days = 1)
        dataToday = getDataByCurrencyAndDate(value, today)
        dataPrew = getDataByCurrencyAndDate(value, prewDay)
        if dataToday is not None and dataPrew is not None:
            if getRate(dataToday) > getRate(dataPrew):
                printData(dataToday, '')
            elif  getRate(dataToday) < getRate(dataPrew):
                printData(dataToday, '')
            else:
                printData(dataToday, '')
    else:
        dataToday = getDataByCurrencyAndDate(value, datetime.date.today())
        if dataToday is not None:
            printData(dataToday, '')


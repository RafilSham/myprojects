from django.shortcuts import render_to_response
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import requests

def get_crypto(args):
    my_money = '1200'
    URL = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    r = requests.get(URL, headers={'X-CMC_PRO_API_KEY': '1134b35c-bfbc-4721-b657-9e7c8c12e2cd'}).text
    r = json.loads(r)
    print('Ваш бюджет :', float(my_money), "$")
    for i in r['data']:
        name = i['name']
        kurs = i['quote']['USD']['price']
        convert = float(my_money) / float(args['Kurs'])
        my_format = '{:>8} {:<21} {:>10} {:<20}  {:>20} {:>8}'
        print(my_format.format('Название:', args['name'], 'Курс в USD:', args['Kurs'], 'Ваш бюджет:', args['convert']))
def show(request):
    args = {}
    get_crypto(args)
    print(args)
    return render_to_response('api.html',{'args':args})


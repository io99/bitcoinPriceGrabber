import requests
r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
print('The current price of Bitcoin is' + ' ' + r.json()['bpi']['USD']['rate'])
#simple program to get the price of bitcoin 
#bpi is top level element, and u can see everything part of bpi
#we want to access USD hence we use this



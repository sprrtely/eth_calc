#!/usr/bin/env python

import requests
import os
import ast
from math import *
from datetime import datetime
from coinmarketcap import Market
# GET /v2/ticker/ETH

def eth_calc():
	url = 'https://api.coinbase.com/v2/prices/ETH-USD/buy'
	response = requests.get(url)
	data = ast.literal_eval(response.text)
	eth_price = data['data']['amount']
	return eth_price
    # if eth_price < 100:
        # print 'time to buy!'
    # elif eth_price >100 and eth_price <250:
        # print 'patience, pet...'
    # else:
        # print 'woohoo! ETH is alive again!'

def main():
	now = datetime.now()
	# define ETH price from eth_calc() function
	price = eth_calc()
    # print timestamp + ETH price
	print '%02d/%02d/%04d %02d:%02d:%02d | ' % (now.month,now.day,now.year,now.hour,now.minute,now.second) + 'ETH = $' + price
	while True:
		eth_input = raw_input('ETH: ')
		xe_eth_usd = float(eth_input) * float(price)
		print xe_eth_usd

        # if eth_input == 'stop':
                # break
# UI
# swap out cb API to cmc API





if __name__ == "__main__":
	main()


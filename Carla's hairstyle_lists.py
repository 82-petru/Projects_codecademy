# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 20:52:04 2019

@author: petru
"""
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]
total_price = 0
for price in prices:
  total_price += price
  average_price = total_price / len(prices)
print(" The price average for haircuts are: %s" % average_price)
new_prices = [cut - 5 for cut in prices]
print(" The new prices for haircuts with 5$ reduction are: ${0}".format( new_prices))
total_revenue = 0
for i in range(0, len(hairstyles)):
  total_revenue += prices[i] * last_week[i]
  average_daily_revenue = total_revenue / 7
print("The average daily revenue is: ${0}".format(average_daily_revenue))
cuts_under_30 = [hairstyles[i] for i in range(0, len(new_prices)) if new_prices[i] < 30]
print("The cuts under 30$ with new prices list: {0}".format(cuts_under_30))
  
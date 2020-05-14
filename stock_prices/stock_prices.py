#!/usr/bin/python

import argparse

def find_max_profit(prices):

  # min_item = max(prices)
  # has to setup with the actual prices or we could start with a profit that will
  # never be reached especially if the max profit is negative(0 > -10)
  max_profit = prices[1] - prices[0]
  # In formal terms, we need to find
  # max(prices[j]−prices[i]),
  # for every i and j such that j > i.

  # min_item was found on the i - 1th round
  
  for i, price in enumerate(prices):
    for j, second_price in enumerate(prices[i+1:]):
      # print(price, second_price, second_price - price > max_profit)
      if(second_price - price > max_profit):
        max_profit = second_price - price
        # print(max_profit)
  return max_profit


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))
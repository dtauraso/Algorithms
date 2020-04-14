#!/usr/bin/python

import argparse

def find_max_profit(prices):

  min_item = prices[0]
  max_item = prices[0]

  for i, price in enumerate(prices):
    if(price < min_item):
      min_item = price
    if(price > max_item):
      max_item = price
  return max_item - min_item
  # pass


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))
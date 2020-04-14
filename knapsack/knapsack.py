#!/usr/bin/python

import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])

def knapsack_solver(items, capacity):

  # print('solver', len(items), capacity)
  [print(i) for i in items]
  capacity_list = [n for n in range(1, capacity)]
  table = [[0 for x in range(capacity)] for y in range(len(items))]
  # I think the table is set up slightly wrong
  # it may also be inittialized incorrectly
  [print(i) for i in table]
  print()
  # make a fake item (0, 0, 0)
  for item in items:
    # we make all the possible knapsacks made from items[0,ith item]
    for c, current_capacity in enumerate(capacity_list):
      # print(item, current_capacity)
      # print(5)
      # print(current_capacity)
      # print(item.size)
      item_index = item.index
      item_size = item.size
      item_value = item.value
      # exactly right amount(just add the one thing)
      if current_capacity - item_size == 0:
        table[i][c] = item_value

      # no room(discard it and use previous value as it's the best we can do)
      elif current_capacity - item_size < 0:
        table[i][c] = table[i][c - 1]

      # we have room for adding an additional item
      elif current_capacity - item_size > 0:
        # thought we always had to include the value once we see there is a fit
        # It's wrong because it may have a lower value than the
        # previous capacity for the same item so we must consider 2 options? still confusing
        # maybe I'm just confused at how a lower value would ever show up

        # we want the max value of these 2 possibilities
        table[i][c] = max(
                          # include the value to our last best value(t[i - 1][c - item_size])
                          item_value + table[i - 1][c - item_size],

                          # exclude the value
                          table[i][c - 1])
    print(table[i])
    print()
  # [print(i) for i in table]
  # pass
def factorial(value):

	from functools import reduce

	return reduce(lambda x, y: x * y, [i for i in range(1, value)])
# print(factorial(100))

# test example from geeks for geeks
# I didn't copy the code(100% derived last night on a whitebaord)
val = [1, 4, 5, 7]
wt = [1, 3, 4, 5]
items = []
for i in range(4):

  items.append(Item(i, wt[i], val[i]))

print(items)
knapsack_solver(items, 7)


if __name__ == '__main__':
  if len(sys.argv) > 1:
    capacity = int(sys.argv[2])
    file_location = sys.argv[1].strip()
    file_contents = open(file_location, 'r')
    items = []

    for line in file_contents.readlines():
      data = line.rstrip().split()
      items.append(Item(int(data[0]), int(data[1]), int(data[2])))
    
    file_contents.close()
    print(knapsack_solver(items, capacity))
  else:
    print('Usage: knapsack.py [filename] [capacity]')
#!/usr/bin/python

import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])

def knapsack_solver(items, capacity):

  # print('solver', len(items), capacity)
  items = [Item(0, 0, 0), *items]

  # [print(i) for i in items]
  capacity_list = [n for n in range(capacity + 1)]

  table = []#[[0 for x in range(capacity)] for y in range(len(items))]
  for y in range(len(items)):
    row = []
    for x in range(capacity + 1):
      row.append(0)
    table.append(row)
  # [print(i) for i in table]
  # print(capacity_list)
  
  # # exit()
  # print()
  # make a fake item (0, 0, 0)
  for i, item in enumerate(items):
    # we make all the possible knapsacks made from items[0,ith item]
    for c, current_capacity in enumerate(capacity_list):
      # print(i, c)
      # print(item, current_capacity)
      # print(5)
      # print(current_capacity)
      # print(item.size)
      item_index = item.index
      item_size = item.size
      item_value = item.value
      # print("capacity", current_capacity, "weight", item_size, 'payoff', item_value)
      # print('difference', current_capacity - item_size)
      # exactly right amount(just add the one thing)
      if current_capacity - item_size == 0:
        table[i][c] = item_value

      # no room(discard it and use previous row's value as it's the best we can do)
      elif current_capacity - item_size < 0:
        table[i][c] = table[i - 1][c]

      # we have room for adding an additional item
      elif current_capacity - item_size > 0:
        # thought we always had to include the value once we see there is a fit(item_value + table[i - 1][c - item_size])
        # It's wrong because it may have a lower value than the
        # previous capacity for the same item so we must consider 2 options? still confusing
        # maybe I'm just confused at how a lower value would ever show up
        # print(item_value + table[i - 1][c - item_size], table[i][c - 1])
        # we want the max value of these 2 possibilities
        table[i][c] = max(
                          # include the value to our last best value(t[i - 1][c - item_size])
                          item_value + table[i - 1][c - item_size],

                          # exclude the value and copy the value from the prev row down
                          table[i - 1][c])
      # [print(i) for i in items]
      # [print(items[i], row) for i, row in enumerate(table)]
    # print()
    # [print((items[i].index, items[i].size, items[i].value), row) for i, row in enumerate(table)]
  # print(('i', 'w', 'v'), [i for i in range(capacity + 1)])
  # [print((f'  {items[i].index} |  {items[i].size} |  {items[i].value}'), " ", row) for i, row in enumerate(table)]
  '''
  go back through the table
  identify all the indexes that point to an item in the solution

  start at table[last_item][c]
  if table[last_item][c - 1] == table[last_item][c]
    jumpt up 1 row 
  '''

  print('retreiving indicies')
  print('final value', table[len(items)-1][capacity])
  temp_capacity = capacity
  ith_item = len(items) - 1
  indicies = {}

  while(temp_capacity > 0):
    # print(ith_item, temp_capacity)
    if(table[ith_item][temp_capacity] == table[ith_item - 1][temp_capacity]):
      ith_item = ith_item - 1
      # if(ith_item < 0):
      #   break
    # ith_item should point to an item included in the solution
    # print(ith_item, items[ith_item])
    # if ith_item < 0:
    #   break
    indicies[ith_item] = 1
    temp_capacity = temp_capacity - items[ith_item].size
  # print('done')
  # print(indicies)

  # items_in_bag = [items[index] for i, index in enumerate(indicies)]

  print(indicies)
  # [print(i) for i in items_in_bag]
  answer = {'Value': table[len(items) - 1][capacity], 'Chosen': indicies}
  return answer
  # return items_in_bag
  # print(capacity)
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
  print("testing", sys.argv)
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
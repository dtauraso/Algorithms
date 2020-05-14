#!/usr/bin/python

import sys

'''

start with 1

1 - 1 = 0  cache[0] = 1
cache[1] = 1

2:
2 - 1 = 1  cache[1] = 1

cache[2] = 1

1
  1 1

2
  2 1's 

3
  3'1's

4
  4 1's 

cache[4] = 1

5
  5 1's
  1 5

  5 - 5 = 0 cache[0] == 1

  5 - 1 = 4 cache[4] = 1

  cache[5] = 2

6
  1 5, 1 1  cache[1]
  6 1's

  6 - 5 = 1 cache[1] == 1

  6 - 1 = 5 cache[5] = 2

  if I just count how many times we are looping then how does that generalize?

  is the answer supposed to be 2?
  cache[6] = 3

7
  7 - 5 = 2  cache[2] = 1
  7 - 1 = 6  cache[6] = 3

  cache[7] = 4
8
  these aren't divisions though
  isn't the point to divide to find out how
  many go into it?

  8 - 5 = 3 cache[3] = 1
  8 - 1 = 7 cache[7] = 4

  cache[8] = 5

9
  1 5, 4 1's   cache[4]

  9 1's

  9 - 5 = 4  cache[4] = 1
  9 - 1 = 8  cache[8] = 5

  cache[9] = 6

10
  10 - 10 = 0 cache[0] = 0
  10 - 5 = 5  cache[5] = 2
  10 - 1 = 9  cache[9] = 6

  cache[10] = 8
12
  1 10, 2 1's 

  the subproblem seems to be
  as the same question for a smaller value
  not ask a subquestion(how many of each denomination does this go into)

  12 - 10 = 2  cache[2] = 1
  12 - 5 = 7   cache[7] = 4
  12 - 1 = 11
19
  1 10, cache[9]

  10 1's

100
  50, 50
  50, 25, 25


for i in denominations:
  if amount >= denominations[i]:
    total += cache[amount - denominations[i]]
cache[amount] = total


temp_amount = amount
how do we know what denominations to pick?

subtract the value off
check the cache
cache[amount-denomination]
we want to add up all the amount_list[current_amount]
we find in the call stack

f():

 for i in range(len(denominations)):

        if(temp_amount >= denominations[i]):
          f()
assume amoun_list has all 0's

for i in denominations:

  for j in range(amount):
    if we can get rid of an ammount
    if amount[j] >= demonination
      set our current amount to 
        the previous amount_list slot that held a solution for subtracting 
        the ith denomination off the jth amount

        +
        the current solution from the last time we visited amount
      amount_list[amount[j]] = amount_list[amount[j] - denominations[i]] + amount_list[amount[j]]
'''
def count_paths(current_amount, denominations, path_count, amount_list):
    
    # we aren't accessing the cache
    # when do we use the cache?
    path_count += amount_list[current_amount]

    if(current_amount == 0):
      # path_count += 1
      return path_count

    else:
      temp_amount = current_amount
      for i in range(len(denominations)):
        if(temp_amount >= denominations[i]):

          path_count = count_paths(
            temp_amount - (temp_amount//denominations[i]),
            denominations[0:i] + denominations[i+1:],
            path_count,
            amount_list)
      return path_count
def making_change(amount, denominations):

  # amount is in cents
  # denominations_cache

  # amount : pennies
  # ammount/ 5: nickels
  # amound/10: dimes
  # have to use some kind of difference because we can't have 
  # 10 pennies and a nickel for 10 cents
  # f(amount % 10) + cach[amount/10]

  # for each option we pick we have to subtract that part of 
    # cache[amount - amount/10]
  # their idea is to have [0,1, 2,..., ammount]
  # loop from 0 to ammount
    # loop from amount - the denominations(make sure the denomination <= amount)
      # subtract off the denomination and access the cache there
      # cache[amount - amound/nth denominaryion]
  amount_list = {i: 0 for i in range(amount+1)}
  amount_list[0] = 1
  amounts = [i for i in range(amount + 1)]

  # assume amoun_list has all 0's except for first one

  for i in range(len(denominations)):

    for j in amounts:
      amount = amounts[j]
      # print(amounts[j], denominations)
      # if we can get rid of an ammount
      if amount >= denominations[i]:
        # set our current amount to 
        #   the previous amount_list slot that held a solution for subtracting 
        #   the ith denomination off the jth amount

        #   +
        #   the current solution from the last time we visited amount
        amount_list[amount] = amount_list[amount - denominations[i]] + amount_list[amount]
    # print(amount_list)
  # amount_list[1] = 1
  # amount_list[2] = 1
  # amount_list[3] = 1
  # amount_list[4] = 1


  # # amount_list[1] = 2
  # # looping through base cases acually messes the cache up
  # print(amount_list)
  # for k, my_ammount in enumerate(range(1, amount)):
  #   # new_way_to_make_change = amount_list[my_ammount]
  #   print('my ammount', my_ammount, denominations, amount_list)
  #   # temp_amount = my_ammount
  #   total = 0
  #   # print('temp ammount', temp_amount, denominations)
  #   for i in range(len(denominations)):
  #     if my_ammount >= denominations[i]:
  #       print(my_ammount, denominations[i])
  #       print('amount_list',
  #       my_ammount - denominations[i],
  #       amount_list[my_ammount - denominations[i]])
  #       total += amount_list[my_ammount - denominations[i]]
  #   print('answer', total)
  #   amount_list[my_ammount] = total

    # new_way_to_make_change = count_paths(temp_amount, denominations, 0, amount_list)
    # print(new_way_to_make_change)
    # for j, denomination in enumerate(denominations):
    #   print('visiting denominations', temp_amount, denomination, j)
    #   # denomination always starts with 1 so temp_amount - (temp_amount//1) = 0
    #   # if(temp_amount >= denomination):
    #   #   new_way_to_make_change += amount_list[
    #   #                                 temp_amount - (temp_amount//denomination)]
    #   #   temp_amount = temp_amount - (temp_amount//denomination)
    #     print(new_way_to_make_change)
    # print()
    # amount_list[my_ammount] = new_way_to_make_change
  # print(amount_list)
  # return amount_list[amount]
  return amount_list[amount]#amount_list
  # pass 

x = making_change(9, [1, 5, 10, 25, 50])
print(x)
if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")
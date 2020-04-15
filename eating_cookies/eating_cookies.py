#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache=None):

  # for i in range(1, n)
  # if i <= 3
    # return cache[i]
  # else
    # return cache[i-1] + cache[i-2] + cache[i-3]?

  '''
  4:
    case (3) + 1
  
  5: 
    case (4) + 1
  
  
  0: 0
  1: 1
  2: 2
  3: 4


  4:
    f(4-3) + f(4-2) + f(4-1)


  1 cookie 2 times
  2 cookies 1 time
  '''
  # 1 way to eat 0 cookies?
  cache = {0: 1, 1: 1, 2: 2, 3: 4}
  # print("n", n)
  if n < 3:
    return cache[n]
  for i in range(1, n+1):
    
    if(i > 3):
      cache[i] = cache[i - 1] + cache[i - 2] + cache[i - 3]
  # print(cache, n)
  # 10562230626642
  # 10562230626642
  # 5742568741225
  return cache[n]
  # pass

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')
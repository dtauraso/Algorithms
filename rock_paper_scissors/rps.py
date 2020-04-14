#!/usr/bin/python

import sys

def spaces(n):
  string = ''
  for i in range(n):
    string += ' '
  return string
def rock_paper_scissors_helper(n, current_list, all_lists):

  if(n == 0):
    # print(f'{spaces(n*2)}done')
    # print(current_list)
    all_lists.append(current_list)
    return all_lists
  rps = ['rock', 'paper', 'scissors']
  for i, item in enumerate(rps):
    # print(f'{spaces(n*2)}{item}')

    all_lists = rock_paper_scissors_helper(
                      n-1,
                      [*current_list, item], all_lists)
  return all_lists
                      
def rock_paper_scissors(n):

  # for each in list
    # call rock_paper_siczors(all remaining)
  # at each level you get 3 different options [rock, paper sizors]

  '''
  n= 2
  rock
      rock
      paper
      scissors
  paper
      rock
      paper
      scissors
  scissors
      rock
      paper
      scissors


  '''
  # if(n == 0):
  #   return
  # rps = ['rock', 'paper', 'scissors']
  # for i, item in enumerate(rps):
  #   print(f'{spaces(n*2)}{item}')

  #   rock_paper_scissors(n-1)
  all_lists = rock_paper_scissors_helper(n, [], [])
  [print(i) for i in all_lists]
  # pass 
rock_paper_scissors(5)

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')
#!/usr/bin/python

import math

def we_have_enough_for_1_batch(recipe, ingredients):
  if(len(recipe.keys() != len(ingredients.keys()))):
    return False
  
  count = 0#len(ingredients.keys())
  for ingredient in recipe:
    if ingredient in ingredients:
      if(ingredients[ingredient] >= recipe[ingredient]):
        count += 1
  
  return count == len(ingredients.keys())

def recipe_batches(recipe, ingredients):
  print(recipe)
  print(ingredients)

  my_ingredients = {*ingredients}

  # taking a recipe
  # subtracting out the ingredients untill we can't 
  number_of_batches = 0
  while(we_have_enough_for_1_batch(recipe, my_ingredients)):
    for ingredient in recipe:
      my_ingredients[ingredient] -= recipe[ingredient]
      number_of_batches == 1
  return number_of_batches
  # pass 


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
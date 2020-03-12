# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    book.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gmachena <gmachena@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/11 10:18:52 by gmachena          #+#    #+#              #
#    Updated: 2020/03/11 16:30:36 by gmachena         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from datetime import datetime
from recipe import Recipe

class Book:

	def __init__(self, name):
		
		if isinstance(name, str):
			self.name = name
		else:
			raise ValueError("Name must be a str")
		self.recipe_list = {"starter": {}, "lunch": {}, "dessert": {}}
		self.last_update = datetime.now()
		self.creation_date = datetime.now()
	
	def __str__(self):
		txt = "______BOOK_____\n\nname: {}\nrecipe_list: {}\nlast_update: \
{}\ncreation_date: {}\n______________\n".format(self.name, \
				self.recipe_list, self.last_update, self.creation_date)
		return txt
	
	def get_recipe_by_name(self, name):
		"""Print a recipe with the name `name` and return the instance"""
		for liste in self.recipe_list:
			for recip in self.recipe_list[liste]:
				if recip is name:
					print(self.recipe_list[liste][recip])
					return (self.recipe_list[liste][recip])
		print("Recipe on get_recipe_by_name not found.")
		return None

	def get_recipes_by_types(self, recipe_type):
		"""Get all recipe names for a given recipe_type """
		for liste in self.recipe_list:
			if liste is recipe_type:
				return self.recipe_list[recipe_type].keys()
		print ("Recipe_type not found on get_recipes_by_types.")
		return None
		

	def add_recipe(self, recipe):
		"""Add a recipe to the book and update last_update"""
		if isinstance(recipe, Recipe):
			self.last_update = datetime.now()
			self.recipe_list[recipe.recipe_type][recipe.name] = recipe
		else:
			raise ValueError("Recipe must be a list.")
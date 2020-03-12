# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gmachena <gmachena@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/11 10:18:57 by gmachena          #+#    #+#              #
#    Updated: 2020/03/11 15:20:00 by gmachena         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Recipe:
	
	def __init__(self, name, cooking_lvl, cooking_time, ingredients, recipe_type, \
		description = ""):
		
		if isinstance(name, str):
			self.name = name
		else:
			raise ValueError("Name must be a str")

		
		if isinstance(cooking_lvl, int):
			self.cooking_lvl = cooking_lvl
		else:
			raise ValueError("cooking_lvl must be an int")

		
		if isinstance(cooking_time, int):
			self.cooking_time = cooking_time
		else:
			raise ValueError("cooking_time must be an int")
		
		if isinstance(ingredients, list):
			self.ingredients = ingredients
		else:
			raise ValueError("ingredients must be a list")
		
		if (recipe_type is "starter" or recipe_type is "lunch" \
			or recipe_type is "dessert") and (isinstance(recipe_type, str)):
			self.recipe_type = recipe_type
		else:
			raise ValueError("recipe_type is a str and can be starter, lunch or dessert")
		
		if isinstance(description, str):
			self.description = description
		else:
			raise ValueError("description must be a str")
			
	def __str__(self):
		""" Return the string print with recipe info"""
		txt = "____RECIPE____\n\nname: {}\ncooking_lvl: {}\ncooking time: {}\nIngredients: {}\nRecipe type: {}\n\
Description:{}\n______________\n".format(self.name, self.cooking_lvl, self.cooking_time, \
			self.ingredients, self.recipe_type, self.description)
		return txt
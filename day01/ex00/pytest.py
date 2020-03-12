# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    pytest.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gmachena <gmachena@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/11 10:18:54 by gmachena          #+#    #+#              #
#    Updated: 2020/03/11 16:21:27 by gmachena         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from book import Book
from recipe import Recipe

rec = Recipe("tourte", 1, 15, ["chocolat", "creme", "oeuf", "farine"], "dessert")
to_print = str(rec)
print(to_print)
book = Book("narnia")
book.add_recipe(rec)
print(book)
recipe_name = book.get_recipe_by_name("tourte")
print(recipe_name)
recipe_type = book.get_recipes_by_types("dessert")
print(recipe_type)
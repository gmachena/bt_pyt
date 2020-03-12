# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gmachena <gmachena@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/09 14:56:20 by gmachena          #+#    #+#              #
#    Updated: 2020/03/09 16:09:19 by gmachena         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import argparse

sandwich = {"ingredients": ["avocado", "arugula", "spinach"], "meal": "lunch", "prep_time": 15}
cake = {"ingredients": ["flour", "sugar", "eggs"], "meal": "dessert", "prep_time": 60}
salad = {"ingredients": ["ham", "bread", "cheese", "tomatoes"], "meal": "lunch", "prep_time": 10}

cookbook = {"sandwich": sandwich, "cake": cake, "salad": salad}

print("Please select an option by typing the corresponding number:\n1: Add a recipe\n2: Delete a recipe\n3: Print a recipe\n4: Print the cookbook\n5: Quit")
rep = input()

parser = argparse.ArgumentParser()
parser.add_argument('integers', metavar='int', type=int, choices=range(5), nargs='+', help='an integer in the range 0..9')
print(parser.parse_args(['1', '2', '3', '4']))


# if rep.isdigit() == 0 or int(rep) < 0 or int(rep) > 5:
#     print("This option does not exist, please type the corresponding number.")
#     while int(rep) != 5:
#         rep = input("To exit, enter 5.\n")
#     exit()


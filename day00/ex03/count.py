# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    count.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gmachena <gmachena@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/09 11:29:07 by gmachena          #+#    #+#              #
#    Updated: 2020/03/09 12:57:16 by gmachena         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import argparse
import string

def text_analyzer(*args):
    car = 0
    low = 0
    upper = 0
    punct = 0
    spaces = 0
    
    if len(args) > 1:
        print("ERROR")
        return 
    elif args == ():
        text = input("What is the text to analyse? ")
    else:
        text = args[0]
    for c in text:
        car += 1
        if c.isupper():
            upper += 1
        if c.islower():
            low += 1
        if c.isspace():
            spaces += 1
        elif c in string.punctuation:
            punct += 1
    print("The text contain ", end="")
    print(car, end="")
    print(" characters:\n\n- ", end="")
    print(upper, end="")
    print(" upper letters\n\n- ", end="")
    print(low, end="")
    print(" lower letters\n\n- ", end="")
    print(punct, end="")
    print(" punctuation marks\n\n- ", end="")
    print(spaces, end="")
    print(" spaces")
    
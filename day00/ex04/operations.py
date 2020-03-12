# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    operations.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gmachena <gmachena@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/09 13:29:52 by gmachena          #+#    #+#              #
#    Updated: 2020/03/09 14:06:38 by gmachena         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import argparse

parser = argparse.ArgumentParser(description="program that prints the results of the four elementary mathematical operations of arithmetic (addition, subtraction, multiplication, division) and the modulo operation.")
parser.add_argument("X", help="premier nombre (int) utilisé pour oprération", type=int)
parser.add_argument("Y", help="deuxieme nombre (int) utilisé pour oprération", type=int)
args = parser.parse_args()

print("Sum:\t\t", end="")
print(args.X + args.Y)

print("Difference:\t", end="")
print(args.X - args.Y)

print("Product:\t", end="")
print(args.X * args.Y)

print("Quotient:\t", end="")
if args.Y != 0:
    print(args.X / args.Y)
else:
    print("ERROR (div by zero)")

print("Remainder:\t", end="")
if args.Y != 0:
    print(args.X % args.Y)
else:
    print("ERROR (modulo by zero)")
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whois.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gmachena <gmachena@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/09 10:38:42 by gmachena          #+#    #+#              #
#    Updated: 2020/03/09 11:21:49 by gmachena         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def whois(argv):
    argv = int(argv)
    if argv == 0:
        print ("I'm Zero.")
    elif argv % 2 == 0:
        print ("I'm Even.")
    else:
        print ("I'm Odd.")

if len(sys.argv) == 2 and sys.argv[1].isdigit():
    whois(sys.argv[1])
else:
    print("ERROR")
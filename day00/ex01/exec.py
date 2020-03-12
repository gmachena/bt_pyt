# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    exec.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gmachena <gmachena@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/09 09:55:53 by gmachena          #+#    #+#              #
#    Updated: 2020/03/09 10:37:41 by gmachena         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

str = ""
revtab = []
i = 0

for arg in sys.argv:
    if i != 0:
        revtab.append(arg[::-1].swapcase())
    i += 1

revtab.reverse()

if i > 1:
    print(*revtab, sep=' ')
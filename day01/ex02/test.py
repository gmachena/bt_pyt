# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gmachena <gmachena@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/12 10:58:34 by gmachena          #+#    #+#              #
#    Updated: 2020/03/12 16:20:04 by gmachena         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from vector import Vector

# test list

z = Vector([12.0, 12.0])
z = Vector([12.0, 12.0, 12.0])
# error list
# z = Vector([12.0])
# z = Vector([12])

values = z.values
size = z.size
print("Vecteur issue d'une liste de taille {}:\n{}\n".format(size, values))

###############

# test int

z = Vector(3)

# error int
# z = Vector(1)
# z = Vector("st")

values = z.values
size = z.size
print("Vecteur issue d'une int de taille {}:\n{}\n".format(size, values))
##############

# test tuple

z = Vector((10,15))

# error tuple
# z = Vector(10,9)
# z = Vector(10.0,15.0)
# z = Vector("st")

values = z.values
size = z.size
print("Vecteur issue d'une tuple de taille {}:\n{}\n".format(size, values))
##############

# vect add
y = Vector([2.0, 3.0 ,4.0, 5.0,6.0])

z + 5.0
y + z
5.0 + y

# error add

# z + 5
# z + Vector(3)

print("Vecteur z de taille {}:\n{}\n".format(z.size, z.values))
print("Vecteur y de taille {}:\n{}\n".format(y.size, y.values))
##############

# vect sub
y = Vector(3)
z = Vector(3)
z - 5.0
y - z
5.0 - y

# error add

# z - 5
# z - Vector(3)

print("Vecteur z de taille {}:\n{}\n".format(z.size, z.values))
print("Vecteur y de taille {}:\n{}\n".format(y.size, y.values))
##############

# vect 

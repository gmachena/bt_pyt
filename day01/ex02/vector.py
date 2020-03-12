# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    vector.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gmachena <gmachena@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/12 10:55:02 by gmachena          #+#    #+#              #
#    Updated: 2020/03/12 15:55:00 by gmachena         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Vector:

    def __init__(self, arg):
        i = 0
        f = 0.0
        self.values = []
        
        if isinstance(arg, list):
            if len(arg) < 2 or any(not isinstance(flt, float) for flt in arg):
                raise ValueError("The vector can't be less than 2 cases and contain float.")
            else:
                self.values = arg
        elif isinstance(arg, int):
            if arg < 2:
                raise ValueError("The vector can't be less than 2.")
            else:
                while i < arg:
                    self.values.append(f)
                    f += 1.0
                    i += 1
        elif isinstance(arg, tuple):
            if len(arg) != 2 or any(not isinstance(nt, int) for nt in arg)\
            or arg[1] - arg[0] < 2:
                raise ValueError("The vector can't be less than 2 and we need 2 int in tuple.")
            else:
                f += arg[0]                
                for i in range(arg[1] - arg[0]):
                    self.values.append(f)
                    f += 1.0
        else:
            raise ValueError("You should be able to initialize the object with a liste, a size or a range.")
        self.size = len(self.values)

    def __add__(self, arg):
        """ add vectors or scal"""
        if isinstance(arg, float):
            self.values[:] = [x + arg for x in self.values]
        elif isinstance(arg, Vector) and arg.size == self.size:
            for x in range(self.size):
                self.values[x] += arg.values[x]
        else:
            raise ValueError("Add with a float or a vector with same case.")

    def __radd__(self, arg):
        """ add vectors or scal if add fail"""
        return self + arg

    def __sub__(self, arg):
        """ sub vectors or scal"""
        if isinstance(arg, float):
            self.values[:] = [x - arg for x in self.values]
        elif isinstance(arg, Vector) and arg.size == self.size:
            for x in range(self.size):
                self.values[x] -= arg.values[x]
        else:
            raise ValueError("Sub with a float or a vector with same case.")
    
    def __rsub__(self, arg):
        """ sub vectors or scal if add fail"""
        return self - arg

    def __truediv__(self, arg):
        """ div vectors or scal"""
        if isinstance(arg, float) and arg != 0:
            self.values[:] = [x / arg for x in self.values]
        else:
            raise ValueError("Div with a float no null.")

    def __rtruediv__(self, arg):
        """ div vectors or scal if add fail"""
        return self / arg

    def __mul__(self, arg):
        """mul vectors or scal"""
        val = 0
        
        if isinstance(arg, float):
            self.values[:] = [x * arg for x in self.values]
        elif isinstance(arg, Vector) and arg.size == self.size:
            for x in range(arg.size):
                val += arg.size[x] * self.size[x]
            return val
        else:
            raise ValueError("mul with a float or a vector with same case.")

    def __rmul__(self, arg):
        """mul vectors or scal if add fail"""
        return self * arg
    
    def __str__(self):
        """"return vector value and his len on str"""
        txt = "vector{} value: {}\n".format(self.size, self.values)
        return txt

    def __repr__(self):
        """representation"""
        return print(self)
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    game.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gmachena <gmachena@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/11 16:31:58 by gmachena          #+#    #+#              #
#    Updated: 2020/03/11 17:09:38 by gmachena         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class GotCharacter:

    def __init__(self, first_character, is_alive = True):
        self.first_character = first_character
        self.is_alive = is_alive

class Stark(GotCharacter):
    """ Stark house"""
    def __init__(self, first_character = None, is_alive=True):
        GotCharacter.__init__(self, first_character, is_alive)
        self.family_name = "Stark"
        self.house_words = "Winter is coming"

    def die(self):
        self.is_alive = False
    
    def print_house_words(self):
        print(self.house_words)
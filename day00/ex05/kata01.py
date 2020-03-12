# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata01.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gmachena <gmachena@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/09 14:11:04 by gmachena          #+#    #+#              #
#    Updated: 2020/03/09 14:20:09 by gmachena         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

languages = {
'Python': 'Guido van Rossum', 'Ruby': 'Yukihiro Matsumoto', 'PHP': 'Rasmus Lerdorf',
}

for kw in languages.items():
    print (*kw)
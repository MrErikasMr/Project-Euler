"""<p>Starting in the top left corner of a $2 \times 2$ grid, and only being able to move to the right and down, there are exactly $6$ routes to the bottom right corner.</p>
<div class="center">
<img src="resources/images/0015.png?1678992052" class="dark_img" alt=""></div>
<p>How many such routes are there through a $20 \times 20$ grid?</p>
"""

import random
import math
# for a 2x2 grid, the rules are:
#can go twice down total
#can go twice up total

# make an array which randomly takes 1 or 0, and the total of the array must be not greater than 2, and also checks to see if that kind of array exists, if it does, delete and try again

array1 = []


grid_length = 5
steps = grid_length * 2
# while True:
#     array2 = []
#     for x in range(steps):
#
#
#         number = random.randint(0,1)
#         array2.append((number))
#
#         if (sum(array2) > grid_length):
#             break
#
#         if (array2 in array1):
#             break
#         if x == (steps -1):
#             if(sum(array2) < grid_length):
#                 break
#             array1.append(array2)
#
#
#     print(array1)
#     print(len(array1))
#
#
#
#        # print("yo")



def formula_for_lattice(r):
    #nCr = n! / (r! * (n-r)!)3
    n = r * 2

    formula = math.factorial(n) / (math.factorial(r) * (math.factorial(n - r)))

    return formula

print(formula_for_lattice(20))


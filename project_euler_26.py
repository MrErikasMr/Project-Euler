# Lexicographic Permutations

"""A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?"""

from itertools import permutations



str = "0123456789"

x = 0
for chars1 in permutations(str):
    print(''.join(chars1))
    x += 1

    if x >= 1000000:
        print("the one-millionth lexicographic permutation of 0123456789 is: ", ''.join(chars1))
        break
"""Prime Digit Replacements
"""

from collections import Counter



word = "hello world"

digit = 50

print(Counter(word))

print(Counter(str(digit)))


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

array = []

for x in range (9999,100000):
    if is_prime(x):
        array.append(x)


array_of_possibilities = ['0','1','2','3','4','5','6','7','8','9']

print(array)

print(len(array))



print(is_prime(563))



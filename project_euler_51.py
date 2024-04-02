"""Prime Digit Replacements
"""

from collections import Counter





def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

array = []
array2 = []

for x in range (9999,100000):
    if is_prime(x):
        array.append(x)
        item1 = str(x)
        for value in range(len(Counter(item1).values())):
            if value > 1:
                array2.append(x)
                break



array_of_possibilities = ['0','1','2','3','4','5','6','7','8','9']

print(array)




print(array2)



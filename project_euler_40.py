import math
from collections import Counter

big_array = []

for x in range(1,1000):
    for y in range(1,x):
        c = math.sqrt(x**2 + y**2)
        string_c = str(c)


        if string_c[-1] == '0' and string_c[-2] == '.':
            print(x,y,c)
            perimeter = x + y + int(c)

            print(perimeter)
            if perimeter <= 1000:
                big_array.append(perimeter)


print(Counter(big_array).most_common())
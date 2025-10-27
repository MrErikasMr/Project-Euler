

"""<p>The number, $1406357289$, is a $0$ to $9$ pandigital number because it is made up of each of the digits $0$ to $9$ in some order, but it also has a rather interesting sub-string divisibility property.</p>
<p>Let $d_1$ be the $1$<sup>st</sup> digit, $d_2$ be the $2$<sup>nd</sup> digit, and so on. In this way, we note the following:</p>
<ul><li>$d_2d_3d_4=406$ is divisible by $2$</li>
<li>$d_3d_4d_5=063$ is divisible by $3$</li>
<li>$d_4d_5d_6=635$ is divisible by $5$</li>
<li>$d_5d_6d_7=357$ is divisible by $7$</li>
<li>$d_6d_7d_8=572$ is divisible by $11$</li>
<li>$d_7d_8d_9=728$ is divisible by $13$</li>
<li>$d_8d_9d_{10}=289$ is divisible by $17$</li>
</ul><p>Find the sum of all $0$ to $9$ pandigital numbers with this property.</p>
"""
from itertools import permutations
positions = [[1,2,3],[2,3,4],[3,4,5],[4,5,6],[5,6,7],[6,7,8],[7,8,9]]

number1 = 1406357288
string_number1 = str(number1)
big_array = []
sum_array = []

for p in permutations('1023456789'):
    num = int(''.join(p))
    big_array.append(num)



#print(positions[0][0])
s = "abcdefghij"  # example string
window = 3        # number of characters per slice


prime_array = [2,3,5,7,11,13,17]
string_array1 = str(big_array[0])

small_array = []











for x in range(len(big_array)):
    string1 = str(big_array[x])

    for i in range(1, len(string1) - window + 1):
        # print(i)
       # print(string1[i:i + window])
       # print(prime_array[i - 1])

        the_number = int(string1[i:i + window])

        if the_number % prime_array[i - 1] == 0:
           # print('yes')
            #print(i)
            pass




        else:
           # print('no')

            break

        if i == 7:
            small_array.append(int(string1))
            print('done')
    # for i in range(len(string1) - window + 1):
    #     print(string1[i:i + window])


    pass


    #print(big_array[x])

print(small_array)

print(sum(small_array))
#print(len(string_number1) == len(set(string_number1)))
#print(big_array)
# for x in range(len(positions)):
#     number2 = ""
#     for y in range(len(positions[x])):
#         number2 = number2 + string_number1[positions[x][y]]
#
#         if y == 2:
#             print(x)
#             print(number2)
#             number2 = int(number2)
#             if x == 0:
#                 if number2 % 2 == 0:
#                     print('yes')
#
#
#             if x == 1:
#                 if number2 % 3 == 0:
#                     print('yes')
#
#             if x == 2:
#                 if number2 % 5 == 0:
#                     print('yes')
#
#             if x == 3:
#                 if number2 % 7 == 0:
#                     print('yes')
#
#             if x == 4:
#                 if number2 % 11 == 0:
#                     print('yes')
#
#             if x == 5:
#                 if number2 % 13 == 0:
#                     print('yes')
#
#             if x == 6:
#                 if number2 % 17 == 0:
#                     print('yes')
#
#
#



#
# for x in range(len(big_array)):
#     if len(str(big_array[x])) <10:
#         big_array.pop(x)


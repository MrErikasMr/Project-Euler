from collections import Counter
## get all the 4-digit prime numbers

#find all the prime numbers which have the same digits

from collections import Counter

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


prime_array = []

for x in range(1000,9999):
    if is_prime(x):
        prime_array.append(x)

#print(prime_array)

length = len(prime_array)



##
first_element = prime_array[0]
cut_array = prime_array[0:10]
#print(cut_array)

new_array = []
x = 0
while True:
    string = str(prime_array[x])
    for z in range(len(prime_array)):
        string2 = str(prime_array[z])
        if (string[0] in string2) and (string[1] in string2) and (string[2] in string2) and (string[3] in string2) and \
                string2[0] in string and string2[1] in string and string2[2] in string and string2[3] in string and string != string2 and Counter(string) == Counter(string2):
           # print(string, string2)
            #print(Counter(string))
            #print(Counter(string2))
            if string not in new_array:

                new_array.append(string)
            if string2 not in new_array:

                new_array.append(string2)

    x += 1
    if x >= 10:
        break



    # for z in range(len(prime_array[y])):
    #     if

#print(new_array)


new_array = sorted(new_array)

#print('yo')
#print(new_array)
tuple_array = tuple(new_array)
#print(tuple_array)

for x in range(len(new_array)):
    new_array[x] = sorted(new_array[x])

#print(new_array)

for x in range(len(new_array)):
    new_array[x] = ''.join(new_array[x])

#print(new_array)
# for x in range(len(new_array)):
#     new_string = ''
#     big_array = []
#     for y in range(len(new_array[:x + 1])):
#         string = str(new_array[y])
#         print(sorted(string))
#         sorted_string = sorted(string)
#         string = ''.join(sorted_string)
#         print(string)
#         print(new_array[y])
#         new_string += string
#         big_array.append(new_string)
#
#         print(new_string)
#         print(big_array)
#
#

#print(Counter(new_array).items())


dictionary1 = Counter(new_array).keys()


index = 0
small_array = []
counter_index = 0
# for keys1 in dictionary1:
#
#
#     for item in keys1:
#         print(item)
#         if item in tuple_array[index]:
#             print("yes")
#         else:
#             print("no")
#     index += 1

print(tuple_array)
print(new_array)

print(new_array[1:])
#
# for x in range(len(new_array)):
#     print(new_array[x+1:])
#     for y in range(new_array[x+1:]):
#         if new_array[x] in new_array
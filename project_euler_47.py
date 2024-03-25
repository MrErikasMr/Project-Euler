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

for x in range(999,10000):
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

counter1 = 0
small_array = []

big_array = []
dict1 = {}
dict2 = {}
string_array = []
for x in range(len(new_array)):
    counter1 = 0
    first_time = True
    string_array = []
    for y in range(len(new_array)):
        if new_array[x] == new_array[y]:
            str_dict = str(new_array[x])
            counter1 += 1
            dict1[str_dict] = counter1

            string_index = str(x)
            string_array.append(string_index)
            dict2[str_dict] = string_array


            string1 = tuple_array[x]
            if first_time:
                big_array.append(string1)


                small_array.append(counter1)
                first_time = False
            small_array[x] = counter1

            string1 += "," + str(tuple_array[x])
            big_array[x] = (string1)




print(dict1)

print(small_array)
print(big_array)

print(len(small_array))
#
# for x in range(len(new_array)):
#     print(new_array[x+1:])
#     for y in range(new_array[x+1:]):
#         if new_array[x] in new_array

print(dict2)

print(dict2.keys())

dict3 = {}

for key in dict2.keys():
    string3 = ""
    first_time = True
    for x in range(len(tuple_array)):
        if key in new_array[x]:
            if first_time:
                string3 = str(x)
                dict3[str(key)] = string3

                first_time = False
            else:

                print(x)
                string3 = string3 + "," + str(x)
                dict3[str(key)] = string3
                print(key)




print(dict3)

for values in dict3.values():
    print(values)


new_array2 = []

print(tuple_array)

print(dict3)
dict_array = []

for values in dict3.values():
    dict_array.append(values)
    print(values)

print(dict_array)

dict4 = {}



count = 0
for values in dict_array:


    print(values)

    print(len(values))

    x = 0
    array = []
    while x < len(values):
        print(array)

        print(values[x])
        if x == len(values) - 2:
            string = values[x:x + 2]
            print(string, 'stirng')
            array.append(int(string))

            x += 2
            print(array)

            dict4[count] = array
            count += 1
            continue



        if x == 0:
            array.append(int(values[x]))
            x+=1
            continue

        if values[x] == ",":
            x += 1
            continue



        if values[x] != ',' and values[x-1] == ',' and values[x+1] == ',':
            array.append(int(values[x]))
            x += 1
            continue

        if values[x] != ',' and values[x-1] == ',' and values[x+1] != ',':

            string = values[x:x+2]
            print(string,'stirng')
            array.append(int(string))

            x+=2
            continue



        x+=1


print(dict_array)
    #
    # for y in range(len(dict_array[x])):
    #     if dict_array[x][y] == ',':
    #         continue
    #     if dict_array[x][y+1] == ",":
    #         tuple(dict_array[x][y])
    #
    #     if dict_array[x][y+1] != ',':
    #         tuple(dict_array[x][y], dict_array[x][y+1])
    # print(dict_array[x])
print(dict4)

big_array2 = []

for values in dict4.values():
    print(values)
    array = []
    for x in range(len(values)):
        array.append(tuple_array[values[x]])
        if x == len(values) - 1:
            big_array2.append(array)

        print(tuple_array[values[x]])


print(tuple_array)
print(big_array2)


for values in big_array2:
    if len(values) == 3:
        print(values)



print(tuple_array)

for numbers in prime_array:
    string_numbers = str(numbers)
    for digit in range(len(string_numbers)):

        
        print(string_numbers[digit])
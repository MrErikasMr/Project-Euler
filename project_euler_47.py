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
dict1 = {}
dict_count = -1
check_array = []
for numbers in prime_array:
    string_numbers = str(numbers)

    dict_count += 1
    new_string = ''
    first_time = True


    for numbers2 in prime_array:
        if numbers2 != numbers:
            string_numbers2 = str(numbers2)
            if Counter(string_numbers) == Counter(string_numbers2):
                if string_numbers not in check_array:

                    new_string += string_numbers
                    check_array.append(string_numbers)

                    new_string += ','
                if string_numbers2 not in check_array:


                    new_string += string_numbers2
                    check_array.append(string_numbers2)

                    new_string += ','
                dict1[dict_count] = new_string

            # new_array.append(string_numbers)
            # break


print(check_array)
dict2 = {}
dict_count2 = -1
for values in dict1.values():
    dict_count2 += 1
    if(len(values) == 20):
        new_string2 = ''
        print(values)
        string = ''
        array = []
        for x in range(len(values) - 1):
            print(values[x])

            if values[x] != ',':
                string += values[x]

            if values[x] == ",":
                array.append(int(string))
                string = ""
                print(array)

            if x == len(values) - 2:
                array.append(int(string))
                string = ""
                print(array)
                dict2[dict_count2] = array

print(dict2)

array3 = []
for values in dict2.values():
    print(values)
    array2 = []

    for x in range(len(values) -1):
        print((values[x+1] - values[x]), (values[x+2] - values[x+1]))

        if (values[x+1] - values[x]) == (values[x+2] - values[x+1]) == values[x+3] - values[x+2]:

            array2.append(values)
            array3.append(array2)
            print(array3)
            print("yooo")
            break
        else:
            break














    # for z in range(len(prime_array[y])):

print(dict1)
print(new_array)


print('yo')
print(array3)



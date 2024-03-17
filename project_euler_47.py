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

print(prime_array)

length = len(prime_array)



##
first_element = prime_array[0]
cut_array = prime_array[0:10]
print(cut_array)

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

print(new_array)
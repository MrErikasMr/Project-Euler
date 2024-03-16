## get all the 4-digit prime numbers

#find all the prime numbers which have the same digits


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


for y in range(length):
    print(prime_array[y])
    for z in range(len(prime_array[y])):
        if 
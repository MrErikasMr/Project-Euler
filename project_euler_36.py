
def sieve_of_eratosthenes(n):
    primes = [True] * ( n +1)
    primes[0] = primes[1] = False

    for i in range(2, int(n**0.5 ) +1):
        if primes[i]:
            for j in range( i *i, n+ 1, i):
                primes[j] = False

    return [i for i in range(2, n + 1) if primes[i]]


# Example usage:
n = 1000000
print("Prime numbers up to", n, "are:", sieve_of_eratosthenes(n))

## take a number, move it's first digit to the end, and keep repeating that n-1 times where n is the number of digits in the number



def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True








circular_prime_array = []

big_array = sieve_of_eratosthenes(1000000)
for x in range(len(big_array)):
    var1 = str(big_array[x])

    original_prime = int(var1)
    if original_prime <= 10:
        circular_prime_array.append(original_prime)
        continue
    if "0" in var1 or "2" in var1 or "4" in var1 or "6" in var1 or "8" in var1:
        continue

    #print(sieve_of_eratosthenes(n)[x],"The prime")

    count = 1
    for y in range(len(var1)-1):
        count += 1

        first_element = var1[0]
        var1 = var1[1:] + first_element


        if is_prime(int(var1)) == False:
            break
           # print("True",var1)



        if count == len(var1):
            circular_prime_array.append(original_prime)






        #now check if all instances are prime


print(circular_prime_array)
print(len(circular_prime_array))
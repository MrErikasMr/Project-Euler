



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
big_array = sieve_of_eratosthenes(n)
print(sieve_of_eratosthenes(n))


trunctable_array = []



for z in range(len(big_array)):
    string1 = str(big_array[z])

    if (len(trunctable_array) >= 11):
        break

    if big_array[z] < 10:
        continue

    can_continue = True

    for a in range(len(string1)):
        potential_prime = int(string1[a:])

        if potential_prime not in big_array:

            break

        # if potential_prime not in big_array:


    if potential_prime not in big_array:
        print(string1)
        continue



    for b in range(len(string1)):
        potential_prime = int(string1[:b+1])
        #print(potential_prime)
        if potential_prime not in big_array:
            break

    if potential_prime not in big_array:
        continue
    else:
        trunctable_array.append(big_array[z])



print(trunctable_array)
print(len(trunctable_array))
print(sum(trunctable_array))
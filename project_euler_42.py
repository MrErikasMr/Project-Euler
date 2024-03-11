big_array = []
small_array = []

def sieve_of_eratosthenes(n):
    primes = [True] * ( n +1)
    primes[0] = primes[1] = False


    for i in range(2, int(n**0.5 ) +1):
        if primes[i]:
            string_i = str(i)

                #small_array = []


            for j in range( i *i, n+ 1, i):
                primes[j] = False

    return [i for i in range(2, n + 1) if primes[i]]






prime_array = sieve_of_eratosthenes(10000)


print(prime_array)



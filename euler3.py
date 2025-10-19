"""<p>The prime factors of $13195$ are $5, 7, 13$ and $29$.</p>
<p>What is the largest prime factor of the number $600851475143$?</p>

"""

global number
global lowest_prime
n = 600851475143





def dividor_machine(n):
    number2 = n
    lowest_prime = 2

    while number2 != 1:
        #print(number2)
        while number2 % lowest_prime != 0:
            lowest_prime += 1
        number2 = int(number2/lowest_prime)

    #print(lowest_prime,"highest")
    return lowest_prime


print(dividor_machine(n))

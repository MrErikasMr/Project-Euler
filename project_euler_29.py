"""<p>Euler discovered the remarkable quadratic formula:</p>
<p class="center">$n^2 + n + 41$</p>
<p>It turns out that the formula will produce $40$ primes for the consecutive integer values $0 \le n \le 39$. However, when $n = 40, 40^2 + 40 + 41 = 40(40 + 1) + 41$ is divisible by $41$, and certainly when $n = 41, 41^2 + 41 + 41$ is clearly divisible by $41$.</p>
<p>The incredible formula $n^2 - 79n + 1601$ was discovered, which produces $80$ primes for the consecutive values $0 \le n \le 79$. The product of the coefficients, $-79$ and $1601$, is $-126479$.</p>
<p>Considering quadratics of the form:</p>
<blockquote>
$n^2 + an + b$, where $|a| &lt; 1000$ and $|b| \le 1000$<br><br><div>where $|n|$ is the modulus/absolute value of $n$<br>e.g. $|11| = 11$ and $|-4| = 4$</div>
</blockquote>
<p>Find the product of the coefficients, $a$ and $b$, for the quadratic expression that produces the maximum number of primes for consecutive values of $n$, starting with $n = 0$.</p>"""

import math

def primes(n,a,b,c):
    print(n)
    c += 1

    primes(c,1,1,c)
  #  return n**2 + a * n + b




#primes(1,1,1,1)



##sieve:

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

def print_primes(n,count):
    count = 0
    num = 2
    while count < n:
        if is_prime(num):
            print(num, end=' ')
            count += 1
        num += 1


a = -1000
b = -1000
results_array = []
results_tuple = ()

string_formula = ""
while True:
    if b >= 1001:
        b = 1
        a += 1



    if a >= 1001:
        break
    for x in range(1, 1000):
        result = (x ** 2) + (a * x) + b

        if is_prime(result) == False:
            if len(results_array) > len(results_tuple):
                results_tuple = tuple(results_array)
                string_formula = ("%s^2 + %s*x + %s"%(x,a,b))
                print(string_formula)

            b += 1



            results_array = []
            break
        results_array.append(result)
        #print(x, result)


print(a)

print(results_tuple)
print(string_formula)
print(len(results_tuple))
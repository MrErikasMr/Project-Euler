"""<p>A Pythagorean triplet is a set of three natural numbers, $a \lt b \lt c$, for which,
$$a^2 + b^2 = c^2.$$</p>
<p>For example, $3^2 + 4^2 = 9 + 16 = 25 = 5^2$.</p>
<p>There exists exactly one Pythagorean triplet for which $a + b + c = 1000$.<br>Find the product $abc$.</p>
"""
import math

"""
3^2 + 4^2 = 5^2

3 + 4 + 5 = 12


(3 + 4 - 12)^2 = (-5)^2
3^2 + 4^2 = 5^2


(3 + 4 - 12)^2 - 3^2 - 4^2 = 0

(a + b - 1000)^2 - a^2 - b^2 = 0"""


for a in range(1000):
    for b in range(1000):
       # print(a,b)
        if(((a + b - 1000)**2) - (a**2) - (b**2) == 0):
           # print(a,b)
            a_plus_b = a+b
            c = 1000 - a_plus_b
            if a_plus_b + c == 1000:
                print(a,b,c)
                print(a*b*c)
                break





"""<p>The prime factors of $13195$ are $5, 7, 13$ and $29$.</p>
<p>What is the largest prime factor of the number $600851475143$?</p>

"""
has_reached_factor = False
count = 0
factors = []
for x in range(1, 600851475143):
    print(x)
    if 600851475143 % x == 0:
        for y in range(2,x -1):
            if has_reached_factor:
                continue
            if x % y == 0:
                has_reached_factor = True
                continue



                print("y: ",y)

        if(has_reached_factor):
            has_reached_factor = False
            continue

        factors.append(x)
        print(factors)
        print(x)
print(factors)
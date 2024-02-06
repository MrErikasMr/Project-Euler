"""<p>The following iterative sequence is defined for the set of positive integers:</p>
<ul style="list-style-type:none;">
<li>$n \to n/2$ ($n$ is even)</li>
<li>$n \to 3n + 1$ ($n$ is odd)</li></ul>
<p>Using the rule above and starting with $13$, we generate the following sequence:
$$13 \to 40 \to 20 \to 10 \to 5 \to 16 \to 8 \to 4 \to 2 \to 1.$$</p>
<p>It can be seen that this sequence (starting at $13$ and finishing at $1$) contains $10$ terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at $1$.</p>
<p>Which starting number, under one million, produces the longest chain?</p>
<p class="note"><b>NOTE:</b> Once the chain starts the terms are allowed to go above one million.</p>
"""



# if number is even:
 #n/2
 #elif number is odd:
 # n * 3 + 1



x = 900000
has_been_1 = False

big_array = []
bigger_array = []

can_x_change = False
z = x

while True:

    if can_x_change:
        z += 1
        x = z
        can_x_change = False
        print(z,"yo")
        if z >= 1000000:
            break



   # print(int(x))


    if x % 2 != 0:
        x = (x*3) + 1
        big_array.append(int(x))
        if x == 1:
           # print(int(x))
            bigger_array.append(big_array)
            big_array = []
            can_x_change = True
            #print(bigger_array)



        continue
    if x % 2 == 0 :
        x = x / 2
        big_array.append(int(x))

        if x == 1:
            bigger_array.append(big_array)
            big_array = []
            can_x_change = True

         #   print(bigger_array)
        continue


print(big_array)
print(bigger_array)

longest_array = max(bigger_array,key=len)
longest_array_index = bigger_array.index(longest_array)
print(longest_array)
print(longest_array_index)
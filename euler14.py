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
global n_array
n_array = []

def collatz_steps_upto(limit=1000000):
    global steps_list
    steps_list = []
    for start in range(1, limit + 1):
        n = start
        n_array.append(n)
        steps = 0
        while n != 1:
            n = 3*n + 1 if n % 2 else n // 2
            steps += 1
        steps_list.append(steps)
    return steps_list

print(collatz_steps_upto(1000000))
max_index = steps_list.index(max(steps_list))
print(max_index)
print(n_array[max_index])

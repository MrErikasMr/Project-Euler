

filename = 'docs\english words.txt'

with open(filename,'r') as file:
    contents = file.read()
    print(contents)

def triangle_formula(n):

    triangle_formula = 0.5 * n * (n + 1)
    return triangle_formula

print(triangle_formula(5))


alphabet = '0ABCDEFGHIJKLMNOPQRSTUVWXYZ'

string = 'SKY'
total_sum = 0

triangle_array = []
for x in range(1,1000):
    triangle_array.append(triangle_formula(x))

print(triangle_array)


for x in range(len(string)):
    index = alphabet.index(string[x])
    print(alphabet.index(string[x]))

    total_sum += index

print(total_sum)



# for x in range words in filename, if sum of letters in triangle array, append to triangle word arrau


big_string = ""

for x in range(len(contents)):
    if contents[x] != '"':
        big_string += contents[x]

print(big_string)

big_array = []

new_string = ""
for x in range(len(big_string)):
    if big_string[x] != ',':
        new_string += big_string[x]
    else:
        total_sum = 0
        for y in range(len(new_string)):
            total_sum += alphabet.index(new_string[y])



        if total_sum in triangle_array:
            big_array.append(new_string)
        new_string = ""
        continue



print(big_array)
print(len(big_array))
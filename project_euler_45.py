#pentagonal numbers

n = 1

pentagonal_array = []

pentagonal_formula = n * (3*n - 1) / 2

broken = False

for n in range(1,100000):
    euler_pentagonal = n * (3 * n - 1) / 2
    pentagonal_array.append(euler_pentagonal)

print(pentagonal_array)

for x in range(len(pentagonal_array)):
    if broken:
        break
    index = pentagonal_array.index(pentagonal_array[x])
  #  print(index)
    for y in range(0,index):

        var1 = pentagonal_array[x]
        var2 = pentagonal_array[y]

        if (var1 + var2) in pentagonal_array and (var1 - var2) in pentagonal_array:

            print(var1,var2)
            broken = True
            break


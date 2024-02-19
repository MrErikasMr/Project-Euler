array = []
abundant_number = []

for x in range(1,28124):
    for y in range(1,x):
        #print(y,"y")
        if x % y == 0:
         #   print(y,"divisible")
            array.append(y)
   # print(x,"x")
  #  print(array)
    if (sum(array) > x):
        abundant_number.append(x)
    array = []



#print(abundant_number)

bigger_array = []
for a in range(len(abundant_number)):
    #print(abundant_number[a])
    number = abundant_number[a]
    to_sum_array = abundant_number[abundant_number.index(abundant_number[a]):]
    #print(to_sum_array)
    for z in range(len(to_sum_array)):
      #  print(number + to_sum_array[z])
        bigger_array.append(number + to_sum_array[z])
   #     print(bigger_array)


print(bigger_array)
biggest_array = []

for i in range(1,28124):
    if i not in bigger_array:
        biggest_array.append(i)

print(biggest_array)
print(sum(biggest_array))


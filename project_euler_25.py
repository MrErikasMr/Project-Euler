array = []
abundant_number = []

for x in range(1,2000):
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



print(abundant_number)


for a in range(len(abundant_number)):
    print(abundant_number[a])
    for z in range(abundant_number[a]):
        print(abundant_number[z])
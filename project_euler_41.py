


number = 1
string = ""
y = 1
for x in range(1,1000001):
    str_x = str(x)

    string += str_x


    if len(string) >= y:
        y *= 10
       # print(string)
        print(string[x -1])

        number *= int(string[x-1])

print(number)
print(string[0])
print(string[9])
print(string[99])
print(string[999])
print(string[9999])
print(string[99999])
print(string[999999])






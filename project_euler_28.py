example1 = 1/6

example2 = 1/7

#print(example2)

string1 = str(example1)
string2 = str(example2)
length_string2 = len(string2)
# print(string2)
# print(string2[2:int((length_string2/2)+2)])
# print(string2[2:8])
# print(string2[8:14])
has_broken = False
y = 3
add_y = False
while True:

    if has_broken:
        break
    for x in range(y,len(string1)):

        formula = (x - 2) + x
        print(x)
        print(string1[y:x])

        if x == (length_string2 /2) + 2:
            y += 1

            break

        if string1[y:x] == string1[x:formula]:
            print("yes")
            print(string1[y:x])
            has_broken = True
            print(x)
            break


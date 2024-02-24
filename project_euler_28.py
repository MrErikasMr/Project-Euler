example1 = 1/6

example2 = 1/7

#print(example2)

string2 = str(example2)
length_string2 = len(string2)
# print(string2)
# print(string2[2:int((length_string2/2)+2)])
# print(string2[2:8])
# print(string2[8:14])
has_broken = False
y = 3
add_y = False
x = y
big_array = []
for x in range(1,1001):

    string1 = str(1/x)
    bad_strings = ["0","."]
    can_detect_bad_strings = True
    looking_for_pattern = False



    if (len(string1)) < 7:
        continue
    print(string1)
    for y in range(len(string1)):

        if looking_for_pattern:
            if first_string == string1[y]:
                if second_string == string1[y+1]:
                    if third_string == string1[y + 2]:
                        big_array.append(string1)
                        break


        if string1[y] in bad_strings and can_detect_bad_strings:
            continue
        else:
            looking_for_pattern = True

            can_detect_bad_strings = False
            first_string = string1[y]
            first_string_index = y
            second_string = string1[y + 1]
            third_string = string1[y + 2]
            print(string1)

            continue
    print(string1)


denominator = 1

#skip the following: 0, dot, 1 until we reach a number that is bigger than 1
#take that number, the 2nd number, and the 3rd number.
#check if the number repeats
#check fi the 2nd number repeats where expected
#check if the 3rd number repeats where expected
#if the expectation is greater than 6, record it.

print(big_array)

from fractions import Fraction


string1 = "13"


string2 = "23"

fractions1 = 1

fraction_array = []

for a in range(len(string1)):
    if string1[a] in string2:
        var = string1[a]

        string1 = string1.replace(var,'',1)
        print(string1)
        string2 = string2.replace(var,'',1)
        print(string2)


if string1 in string2:
    print("yes")

for x in range(10,100):

    for y in range(10,x + 1):


        if x == y:
            continue

        string_x = str(x)
        string_y = str(y)
        original_string_x = string_x
        original_string_y = string_y
        #
        # print(string_x + " / " + string_y)
        # print(x/y)

        factor1 = y / x


        for a in range(len(string_x)):
            if string_x[a] in string_y:
                #print(string_x + " / " + string_y)

                var = string_x[a]



                string_x = string_x.replace(var, '', 1)
                string_y = string_y.replace(var, '', 1)



                if string_x == "0":
                    break

                else:
                    numerator = float(string_y)
                    denominator = float(string_x)
                    factor2 = numerator / denominator
                   # print(string_x + " / " + string_y)


                    if factor1 == factor2:



                        if "0" not in original_string_x:
                            print(factor1)
                            print(factor2)
                            print(original_string_y + " / " + original_string_x)
                            print(string_y + " / " + string_x)
                            print("yo")

                            fractions1 *= factor1
                            fraction_array.append((original_string_y,original_string_x))




                break







print(fractions1)

fractions1 = Fraction(fractions1).limit_denominator()


print(fractions1)

print(fraction_array)


num1 = 1
den1 = 1
for z in range(len(fraction_array)):
    print(fraction_array[z][0])
    print(fraction_array[z][1])
    num1 *= float(fraction_array[z][0])
    den1 *= float(fraction_array[z][1])



print(num1)
print(den1)
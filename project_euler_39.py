#create a loop which creates pandigitals until length is 9



a = 0
string1 = "1"
broken = False

big_array = []
while True:
    string = ""
    a += 1


    for x in range(1,100):
      #  print(a*x)
        product = a * x
        string_product = str(product)
        broken = False
        if x == 1 and string_product[0] != "9":
            break

        for y in range(len(string_product)):

            if string_product[y] == '0':
                broken = True
                break
            if string_product[y] not in string:
                string += string_product[y]

            else:
              #  print('yes',string_product[y],string_product,string)
                broken = True

                break

        if broken:
            broken = False
           # print(big_array)
            break
        if len(string) >= 9:
            if len(string) > 9:
                break
            big_array.append(string)
            print(big_array)
            break












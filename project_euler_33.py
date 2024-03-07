
total_sum = 0
total_sum_array = []
big_array = []
for x in range(1,6000):
    for y in range(1,x):
        string_x = str(x)
        string_y = str(y)
        product = x * y
        string_product = str(product)

        sum_of_lengths = len(string_x) + len(string_y) + len(string_product)
        actual_string = string_x + string_y + string_product

        if (sum_of_lengths == 9) and '0' not in actual_string:

           # print(string_x + " x " + string_y + " = " + string_product)

            #  print(actual_string)

            big_array.append(product)


  #          print(actual_string)

 #           prin   t(string_x + " x " + string_y + " = " + string_product)


#            print(sorted(actual_string))

            string = ""
            actual_string = sorted(actual_string)


            for z in range(len(actual_string)):
              #  print(actual_string[z])
                if actual_string[z] not in string:
                    string += actual_string[z]
                else:
                    break
              #  print(string)

            if len(string) >= 9:

             #   print(string)
              #  print(sorted(string))
                print(actual_string)
                total_sum += product
                print (string_x + " x " + string_y + " = " + string_product)
                print(product)
                string = ""
            else:
                continue
            if product not in total_sum_array:
                total_sum_array.append(product)





print(len(big_array))
print(total_sum)
print(sum(total_sum_array))
print(total_sum_array)

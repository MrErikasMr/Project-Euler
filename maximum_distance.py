class MaximumDistance:
    def __init__(self):
       # self.my_list = [5,4,3,2,1,0,5]
        self.my_list = [9,2 ,3 ,4 ,5 ,6 ,7 ,8 ,18 ,0]
        self.my_list = [34, 8, 10, 3 ,2 ,80, 30, 33 ,1]
        self.my_dict = {}

    def sort_list(self, my_list):
        new_list = []

        for x in range(len(my_list)):
            if my_list[x + 1] > my_list[x]:
                new_list.append(my_list[x])
                new_list.append(my_list[x + 1])
                return new_list

        return new_list

    def get_distance(self):
        return 1

    def return_dict(self):
        return {}

    def expand_dict(self, my_list, my_dict):
        for x in range(len(my_list)):
            my_dict[str(x)] = []
        return my_dict


    def list_differences(self, my_list,my_dict):
      #  print(my_list)
        for y in range(len(my_list)):
            new_array = []

            for x in range(len(my_list[y:])):
                if(x == (len(my_list[y:]) - 1)):
                    break
                result =  my_list[y:][x+1] - my_list[y:][0]

                new_array.append(result)
                my_dict[str(y)] = new_array

        return my_dict









    def populate_dict(self, my_dict, my_list):
        for x in range(len(my_list)):

            pass
        pass
        #return my_dict



    def for_each_number_last_biggest_new_number(self, my_list):
        pair_array = []
        index_array = []
        for x in range(len(my_list)):
            for y in range(len(my_list[x:])):
                try:
                    if(my_list[x + y+1]) > my_list[x]:
                        print("yes", my_list[x], " ", my_list[x + y + 1], "X index: ", x, ", y index: ", x + y + 1)
                        if not pair_array:
                            pair_array.append(my_list[x])
                            pair_array.append(my_list[x + y + 1])
                            index_array.append((x + y + 1) - x)
                        else:
                            if index_array[-1] > ((x+y+1) - x):
                                continue
                            else:
                                index_array = []
                                pair_array = []
                                index_array.append((x + y + 1) - x)
                                pair_array.append(my_list[x])
                                pair_array.append(my_list[x + y + 1])








                    else:
                        print("no", my_list[x], " ", my_list[x + y + 1])
                except IndexError:
                    print("indexError")
                    continue
        return pair_array, index_array



instance1 = MaximumDistance()

print(instance1.list_differences(instance1.my_list,instance1.my_dict))

my_dict2 = instance1.list_differences(my_list=instance1.my_list,my_dict=instance1.my_dict)


highest_value = max(my_dict2)
key_with_highest_value = max(my_dict2, key=lambda k: my_dict2[k])

print(instance1.for_each_number_last_biggest_new_number(instance1.my_list))


#print(key_with_highest_value)
#print(my_dict2[key_with_highest_value])
#print(my_dict2[key_with_highest_value].index(max(my_dict2[key_with_highest_value])))
#print(instance1.my_list[int(key_with_highest_value)],)
print(instance1.my_list)
print(instance1.for_each_number_last_biggest_new_number(instance1.my_list))

#print(instance1.sort_list(instance1.my_list))
#print(instance1.expand_dict(instance1.my_list,instance1.my_dict))

#print(instance1.populate_dict(my_dict=instance1.expand_dict(instance1.my_list,instance1.my_dict)))
#comparing 2 numbers, right next to each other other, and trying to find the pair that is right next to each other, where list[x] < list[x+1]
#next challenge is to find the next number in the series that is bigger, regardless if it is right next to the original list[x] number
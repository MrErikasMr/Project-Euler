from maximum_distance import MaximumDistance

instance = MaximumDistance()
list1 = instance.my_list
dict1 = instance.my_dict


def test_get_distance():
    #distance should be integer

    result = instance.get_distance()
    assert type(result) is int


def test_get_list():
    #list should be list

    result = list1
    assert type(result) is list


def test_return_dict():

    result = instance.return_dict()
    assert type(result) is dict

def test_expand_dict():

    #assertions are:
    #returns dict
    #returns dict with number of keys equal to array
    result = instance.expand_dict(my_list=instance.my_list, my_dict= instance.my_dict)
    assert len(list1) == len(dict1)

def test_list_differences():
    #list1 = [0,5,6,2]
    #result: [5,6,2,1,-3,-4]

def test_populate_dict():
    pass
    #mock_list = [0,5,6,2]
    #mock_dict = {
###       "0" : [5,6,2],
        #"1": [1,-3],
        #"2": [-4]
#   }



# def test_is_next_bigger():
#     #checks if 1st element is bigger than 0th element
#     assert list1[1] > list1[0]

# def test_sort_list_returns_list():
#     #returns the list
#
#     assert instance.sort_list(list1) == list1


def test_sort_list_checks_if_next_number_bigger():
    assert instance.sort_list(list1) == [0,5]


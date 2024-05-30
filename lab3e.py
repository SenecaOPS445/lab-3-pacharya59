#!/usr/bin/env python3
#Author ID: pacharya9(100706225)

#Creating a list called my_list
my_list = [100, 200, 300, 'six hundred']

#Creating a function that returns all the items in the global list.
def give_list():
    list_copy = my_list[0:]
    return list_copy

#Creating another function that returns the first item from the global list.
def give_first_item():
    first_item = str(my_list[0])
    return first_item

#Creating another function that returns first and last item from the list.
def give_first_and_last_item():
    first_last = [my_list[0], my_list[-1]]
    return first_last

#Creating one more function that returns second and third last item.
def give_second_and_third_item():
    second_third = [my_list[-3], my_list[-2]]
    return second_third

if __name__ == '__main__':
    print(give_list())
    print(give_first_item())
    print(give_first_and_last_item())
    print(give_second_and_third_item())


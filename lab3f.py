#!/usr/bin/env python3

my_list = [1,2,3,4,5]

def add_item_to_list(ordered_list):
    next_item = my_list[-1] + 1
    return my_list.append(next_item)

def remove_items_from_list(ordered_list, items_to_remove):
    for element in items_to_remove:
        new_list = my_list.remove(element)

    return new_list

if __name__ == '__main__':
    print(my_list)
    add_item_to_list(my_list)
    add_item_to_list(my_list)
    add_item_to_list(my_list)
    print(my_list)
    remove_items_from_list(my_list, [1,5,6])
    print(my_list)


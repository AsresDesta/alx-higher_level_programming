#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    bootlist = my_list[:]
    for count, i in enumerate(my_list):
        if i % 2 == 0:
            bootlist[count] = True
        else:
            boolist[count] = False
    return(boolist)

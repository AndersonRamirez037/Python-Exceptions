#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    length = 0
    try:     
        for i in range(0,x):    
            print(my_list[i],end = "")
            length += 1 
        print()
    except Exception: 
        print()
    return length
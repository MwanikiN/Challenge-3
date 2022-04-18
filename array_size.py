""" NumPy program to create an array with at least 5 user input integers and
determine the size of the memory occupied by the array. """
import numpy as np
def arr_size():
    my_list = []
    n = int(input("Number of elements: "))
    print("Key {} elements" .format(n))
    for i in range(n):
        elements = int(input())
        my_list.append(elements)
    my_array = np.array(my_list) 
    memory_size = my_array.itemsize #one element memory size
    array_size = my_array.nbytes
    return  memory_size, array_size


print(arr_size())
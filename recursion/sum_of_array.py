def sum_of_array(arr):
    if len(arr) == 0:
        return 0
    
    return arr[0] + sum_of_array(arr[1:])
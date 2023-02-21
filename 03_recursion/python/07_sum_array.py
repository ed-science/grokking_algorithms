def sum_array(arr):
    return arr[0] + sum_array(arr[1:]) if arr else 0
def find_max(arr):
    if len(arr) == 0:
        return 0
    elif len(arr) == 1:
        return arr[0]
    elif len(arr) == 2:
        return max(arr[0], arr[1])
    sub_max = find_max(arr[1:])
    return max(arr[0], sub_max)

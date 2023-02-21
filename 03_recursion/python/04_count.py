def count(arr):
    return 1 + count(arr[1:]) if arr else 0
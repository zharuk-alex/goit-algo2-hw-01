def min_max_arr(arr):
    if len(arr) == 0:
        return None, None

    elif len(arr) == 1:
        return arr[0], arr[0]

    elif len(arr) == 2:
        if arr[0] < arr[1]:
            return arr[0], arr[1]
        else:
            return arr[1], arr[0]

    mid = len(arr) // 2
    left_min, left_max = min_max_arr(arr[:mid])
    right_min, right_max = min_max_arr(arr[mid:])

    min_val = left_min if left_min < right_min else right_min
    max_val = left_max if left_max > right_max else right_max

    return min_val, max_val


# arr = []
# arr = [3]
arr = [38, 27, 43, 3, 9, 82, 10]
min_num, max_num = min_max_arr(arr)
print(f"min: {min_num}, max: {max_num}")

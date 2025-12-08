def find_max_min(arr):
    max_val = arr[0]
    min_val = arr[0]
    
    for i in arr:
        if i > max_val:
            max_val = i
        if i < min_val:
            min_val = i
    return max_val, min_val

nums = list(map(int, input().split()))
mx, mn = find_max_min(nums)
print(mx, mn)
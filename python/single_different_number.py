def stray(arr):
    for i in arr:
        if arr.count(i) == 1:
            print(f"Single element of list: {i}")


stray([1, 1, 1, 1, 1, 1, 54])

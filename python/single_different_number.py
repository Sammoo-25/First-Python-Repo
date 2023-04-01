def stray(arr):
    # sort_list = sorted(arr)
    # j = 0
    # for i in range(len(sort_list) - 1):
    #     j += 1
    #     if sort_list[i] == sort_list[j]:
    #         continue
    #     else:
    #         print(f"Single element of list: {sort_list[j]}")
    #         break
    a = arr[0]
    for i in range(len(arr) + 1):
        if a == i:
            continue
        else:
            print(f"Single element of list: {arr[i]}")
            break


stray([1, 1, 1, 1, 5, 1, 1])

def order(sentence):
    arr = sentence.split()
    ls = []
    for i in arr:
        for j in i:
            if j.isnumeric():
                ls.append(int(j))
    for i in range(len(ls) - 1):
        for k in range(len(ls) - i - 1):
            if ls[k] > ls[k + 1]:
                ls[k], ls[k + 1] = ls[k + 1], ls[k]
                arr[k], arr[k + 1] = arr[k + 1], arr[k]
    return ' '.join(arr)
print("This is dev_q ")
print("dev_q")
print("branch")

print(order("is2 Thi1s T4est 3a"))

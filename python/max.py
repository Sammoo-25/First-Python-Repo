import random

n = random.randint(1, 10)
arr = []
for i in range(n):
    i = random.randint(10, 100)
    arr.append(i)
print(f"List: {arr}")
print(f"This is max number of list: {max(arr)}")

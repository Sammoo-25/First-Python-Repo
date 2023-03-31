import random

n = random.randint(1, 10)
arr = []
for i in range(n):
    i = random.randint(10, 100)
    arr.append(i)
print(f"List: {arr}")
print(f"This is sum number of list: {sum(arr)}")

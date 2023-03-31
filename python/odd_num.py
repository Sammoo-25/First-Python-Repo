import random

n = random.randint(1, 10)
arr = []
for i in range(n):
    i = random.randint(10, 100)
    arr.append(i)
print(f"List: {arr}")
odd = []
for j in arr:
    if j % 2 == 1:
        odd.append(j)
print(f"This is odd numbers list from 'arr': {odd}")
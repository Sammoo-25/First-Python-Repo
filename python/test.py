# n = 8
# sum = 0
# for i in range(n+1):
#     sum += i
# print(f"Sum: {sum}")
import math

# def summation(num):
#     return sum(i for i in range(num+1))
# print(summation(8))


# arr = [20, 10, 30, 10, 10, 15, 35]
#
#
# def find_even_index(nums):
#     for i in range(len(arr)):
#         if sum(arr[:i]) == sum(arr[i + 1:]):
#             return i
#     return -1

# print(find_even_index(arr))

# for ind, ele in enumerate(arr):

# sum2 = 0
# for i in range(len(arr)):
#     sum1 = sum(range(0,len(arr) // 2))
# print(sum1)

# a = 152896
# res = list(map(int, str(a)))
# res.sort(reverse=True)
# digit_str = ''.join(map(str, res))
# digit_int = int(digit_str)
# print(digit_int)


# l = [19, 5, 42, 2, 77]
# f = l.pop(l.index(min(l)))
# g = l.pop(l.index(min(l)))
# print(f + g)

# l = [19, 5, 42, 2, 77]
# k = []
# for i in range(len(l)):
#     k += [math.pow(i,l[i])]
# print(*k)


# a = [1, 2, 2,3,3]
# b = [2,3]
# for i in b:
#     while i in a:
#         a.remove(i)

# for i in b:
#     if i in a:
#
a = "Success"
l = a.split()
for i in a:
    print(l.countof(i))
# for i in a:
#     if a.count(i) == 1:
#         a = a.replace(i, "(")
#     elif a.count(i) > 2:
#         a = a.replace(i, ")")
#print(a)
# if a.count(a[0]) == 1:
#     print(a.replace(a[0], "("))
# else:
#     print(a.replace(a[0], ")"))

def duplicate_count(text):
    li = list(text.lower())
    res = {}
    count = 0
    for i in li:
        res[i] = li.count(i)
    for key in res:
        if res[key] > 1:
            count += 1
    return count

print("Hello")
print("World")
print("!!!!!")


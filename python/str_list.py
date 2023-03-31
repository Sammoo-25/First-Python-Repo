vowel = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]
str = "rInsHccjQwHNLHFUlDnUaAa"
str.lower()
ls = []
for i in str:
    if i in vowel:
       ls.append(i)
print(f"List of vowel letters: {ls}")
print(f"Count of vowel letters in 'ls': {len(ls)}")

#print(*vowel)
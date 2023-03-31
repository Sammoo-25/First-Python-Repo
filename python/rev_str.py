def reverse_words(text):
    wordlist = text.split(' ')

    def revers_word(w):
        rev_w = w[::-1]
        return rev_w

    rev_list = []
    for i in wordlist:
        rev_list.append(revers_word(i))
    return ' '.join(rev_list)


text = "Hello This is Reverce String"
print(reverse_words(text))

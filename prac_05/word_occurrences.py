words_in_text = {}

get_text = input("Enter text: ")

words = get_text.split()
for word in words:
    if word in words_in_text:
        words_in_text[word] += 1
    else:
        words_in_text[word] = 1

sorted_words = dict(sorted(words_in_text.items()))
print(sorted_words)

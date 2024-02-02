def count_words(input_string):
    words = input_string.split()
    return len(words)

user_input = input("")
##
word_count = count_words(user_input)
print(word_count)
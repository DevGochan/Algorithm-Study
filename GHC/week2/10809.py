al_list = [-1] * 26
word = input()

for char in word:
    index = ord(char) - 97
    if al_list[index] == -1:
        al_list[index] = word.index(char)

output_str = ' '.join(map(str, al_list))
print(output_str)

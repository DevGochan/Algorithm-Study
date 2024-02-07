from string import ascii_lowercase
L = list(ascii_lowercase)

S = input()

for i in L:
    if i in S:
        print(S.index(i), end= ' ')
    else:
        print( -1, end =' ')
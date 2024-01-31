word = input().upper()
count = {}
for char in word :
    if char in count :
        count[char] += 1
    else :
        count[char] = 1
maxkey = max(count, key = count.get)
maxvalue = count[maxkey]
count.pop(maxkey)
if maxvalue in count.values():
    print("?")
else :
    print(maxkey)
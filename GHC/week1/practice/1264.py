lines = []

while True :
    line = input()
    if line == "#":
        break
    lines.append(line)

for line in lines :
    count = 0
    count += line.lower().count('a')   
    count += line.lower().count('e')   
    count += line.lower().count('i')   
    count += line.lower().count('o')   
    count += line.lower().count('u')   
    print(count)
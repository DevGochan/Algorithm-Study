Dajangjo = input()
Numbers = Dajangjo.split()
if Numbers == sorted(Numbers) :
    print("ascending")
elif Numbers == sorted(Numbers, reverse= True) :
    print("descending")
else :
    print("mixed")
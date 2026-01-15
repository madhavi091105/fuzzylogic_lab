a = input("Enter the set of characters: ")
b = input("Enter the sentence: ")
s = set(b.replace(" ",""))
if set(a).issubset(s):
    print("Valid")
else:
    print("Not valid")

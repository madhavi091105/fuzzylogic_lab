allowed = input("enter allowed didgits: ")
a = set(allowed)
s = input("enter string: ")
valid = True
for i in range(len(s)):
    if s[i] not in a:
        valid = False
        break
if valid:
    print("Valid")
else:
    print("Invalid")
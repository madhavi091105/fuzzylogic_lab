a = int(input("Enter the number n: "))
set1 = set()
set2 = set()
set3 = set()
for i in range(a):
    if i % 7 == 0:
        set1.add(i)
    elif i % 5 == 0:
        set2.add(i)
    elif i % 3 == 0:
        set3.add(i)
b = (set1 & set2) | set3
print(b)

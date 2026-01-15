a = set(map(int,input("Enter the list of employees in A: ").split()))
b = set(map(int,input("Enter the list of employees in B: ").split()))
te = a | b
be = a & b
print("Total employees: ",len(te))
print("Employees in a: ",len(a))
print("Employees in b: ",len(b))
print("Employees in both: ",len(be))


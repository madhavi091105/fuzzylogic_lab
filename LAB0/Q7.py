A = eval(input("Enter list for course A: "))
B = eval(input("Enter list for course B: "))
C = eval(input("Enter list for course C: "))
N = int(input("Enter total number of students: "))
setA = set(A)
setB = set(B)
setC = set(C)
enrolled_any = setA | setB | setC
enrolled_3 = setA & setB & setC
enrolled_2 = ((setA & setB) | (setB & setC) | (setA & setC) - enrolled_3)
enrolled_1 = enrolled_any - enrolled_2 - enrolled_3
not_enrolled = N - len(enrolled_any)
print("not enrolled:",not_enrolled)
print("enrolled in one course:",len(enrolled_1))
print("enrolled in two courses:", len(enrolled_2))
print("enrolled in three courses:", len(enrolled_3))

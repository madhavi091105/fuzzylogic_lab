n = int(input("Enter number of groups:"))
unique_groups = set()
for _ in range(n):
    group = list(map(int,input().split()))
    unique_groups.add(tuple(sorted(group)))
print("Total number of distinct groups: ",len(unique_groups))
    
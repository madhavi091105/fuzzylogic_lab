groups = eval(input("Enter the groups: "))
unique_groups = set()
for group in groups:
    sorted_groups = tuple(sorted(group))
    unique_groups.add(sorted_group)
print("Total number of distinct groups:",len(unique_groups))
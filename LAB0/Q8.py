
n = int(input("Enter number of groups: "))
groups = []
for i in range(n):
    group = list(map(int, input().split()))
    groups.append(set(group))
merged = []
for group in groups:
    found = False
    for m in merged:
        if group & m:          
            m.update(group)    
            found = True
            break
    if not found:
        merged.append(group)
changed = True
while changed:
    changed = False
    result = []
    while merged:
        first = merged.pop()
        for other in merged[:]:
            if first & other:
                first |= other
                merged.remove(other)
                changed = True
        result.append(first)
    merged = result
print(len(merged))

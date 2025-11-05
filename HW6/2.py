l = [1, 2, 3, 4, 5]
n = 1
conv = []
used = set()

lng = len(l)
for i in range(lng):
    if l[i] in used:
        continue
    found = False

    for j in range(i+1, lng):
        if l[j] in used:
            continue
        if (l[i] + l[j] == n):
            conv.append([l[i], l[j]])
            used.add(l[i])
            used.add(l[j])
            found = True
            break
    if not found and l[i] == n:
        conv.append(l[i])
        used.add(l[i])
        
            

print(conv)
entry = []
out = []

idx = 0
for x in range(len(entry)):
    temp = []
    for i in range(len(entry)):
        a = entry[-1-i][idx]
        temp.append(a)
    idx += 1
    out.append(temp)

print(out)

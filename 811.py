a = input()
b = []
q = []
for i in range(0, len(a)):
    q.append(a[i])
    if a[i] == '3':
        b.append(1)
    if a[i] == '4':
        b.append(1)
    if a[i] == '5':
        b.append(1)
print(q, sum(b), (sum(b)/len(a))*100)
a = int(input())
b = set()
ab = set()
c = a
while c > 0:
    k = int(input())
    s = c - k
    h = set()
    for i in range(1, k+1):
        m1 = input()
        h.add(m1)
    if len(b) == 0:
        b = b|h
    else:
        b.intersection_update(h)
    ab = ab|h
print(b, ab)
def a(x, k):
    if x <140:
        return (k+1)
    else: return a(x-140, k+1)
def w(p,f):
    if f==0:
        return p+4
    return w(p+0.25, f-1)
d = a(1000, 0)
s = w(0, d)
print(s)
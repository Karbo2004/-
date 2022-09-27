Q = int(input())
W = Q % 10
E = Q%100 - W
R = (Q% 1000 - W-E)/100
print(int(W*100+E+R))



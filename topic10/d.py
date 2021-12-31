def dist(x, y, p):
    s = 0
    for a, b in zip(x, y):
        s += abs(a - b) ** p
    return s ** (1 / p)


N = int(input())
X = list(map(int, input().split()))
Y = list(map(int, input().split()))
print("{:.6f}".format(dist(X, Y, 1)))
print("{:.6f}".format(dist(X, Y, 2)))
print("{:.6f}".format(dist(X, Y, 3)))
tmp = []
for n in range(N):
    tmp.append(abs(X[n] - Y[n]))
chebyshev = max(tmp)
print("{:.6f}".format(chebyshev))

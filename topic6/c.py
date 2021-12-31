n = int(input())
X = [[[0] * 10 for f in range(3)] for b in range(4)]
for i in range(n):
    b, f, r, v = map(int, input().split())
    X[b - 1][f - 1][r - 1] += v


for i, building in enumerate(X, 1):
    for floor in building:
        print("", *floor)
    if i != 4:
        print("#" * 20)

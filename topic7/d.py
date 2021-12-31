n, m, l = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]
B = [list(map(int, input().split())) for _ in range(m)]
for i in range(n):
    for j in range(l):
        ci = 0
        for k in range(m):
            ci += A[i][k] * B[k][j]
        print(f"{ci} " if j != l - 1 else ci, end="")
    print()

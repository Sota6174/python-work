r, c = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(r)]
for i in range(r):
    table[i].append(sum(table[i]))
table.append([0 for i in range(c + 1)])
for i in range(r):
    for j in range(c + 1):
        table[-1][j] += table[i][j]
    print(*table[i])
print(*table[-1])

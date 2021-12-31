n = int(input())
X = [[0] * 13 for i in range(4)]
table = {'S': 0, 'H': 1, 'C': 2, 'D': 3}
for i in range(n):
    pattern, num = input().split()
    num = int(num) - 1
    X[table[pattern]][num] = 1

table = {0: 'S', 1: 'H', 2: 'C', 3: 'D'}
for i in range(4):
    for j in range(13):
        if X[i][j] == 0:
            print('{} {}'.format(table[i], j + 1))

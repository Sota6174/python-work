import itertools


while True:
    n, x = map(int, input().split())
    if n == 0 and x == 0:
        break
    count = 0
    for c in itertools.combinations(range(1, n + 1), 3):
        if sum(c) == x:
            count += 1
    print(count)

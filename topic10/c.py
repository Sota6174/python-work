import math

while True:
    n = int(input())
    if n == 0:
        break
    points = list(map(int, input().split()))
    m = sum(points) / n # 平均
    s2 = sum((a - m) ** 2 for a in points) / n
    print(f"{math.sqrt(s2):.8f}")

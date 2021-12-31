x1, y1, x2, y2 = map(float, input().split())
dx = abs(x1 - x2) ** 2
dy = abs(y1 - y2) ** 2
print(f"{(dx + dy) ** 0.5:.8f}")

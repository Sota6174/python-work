import math

a, b, C = map(int, input().split())
theta = math.radians(C)
S = 0.5 * a * b * math.sin(theta)
c = math.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos(theta))
h = b * math.sin(theta)
print(f"{S:.9f}\n{a + b + c:.9f}\n{h:.9f}")

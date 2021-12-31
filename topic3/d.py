a, b, c = map(int, input().split())
count = 0
for i in range(a, b + 1):
    if c % i == 0:
        count += 1
print(count)

# 約数列挙
# divisor = [i for i in range(1, c + 1) if c % i == 0]
# print(divisor)

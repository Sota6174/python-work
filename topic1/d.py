# Sample Input, Sample Output
# 46979, 13:2:59

S = int(input())
print(f"{S // 3600}:{(S % 3600) // 60}:{(S % 3600) % 60}")

# m, s = divmod(S, 60)
# h, m = divmod(m, 60)
# print(h, m, s, sep=':')

import sys
from collections import Counter

s = sys.stdin.read().lower()
c = Counter(s)
for i in range(97, 123):
    print(f"{chr(i)} : {str(c[chr(i)])}")

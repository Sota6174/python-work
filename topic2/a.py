a, b = map(int, input().split())
if a > b:
    operator = '>'
elif a < b:
    operator = '<'
else:
    operator = '=='
print("a {} b".format(operator))

# if a > b:
#     print("a > b")
# elif a < b:
#     print("a < b")
# else:
#     print("a == b")

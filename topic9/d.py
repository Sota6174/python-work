s = input()
for i in range(int(input())):
    cmd, a, b, *p = input().split()
    a = int(a)
    b = int(b) + 1
    if cmd == 'print':
        print(s[a:b])
    elif cmd == 'reverse':
        s = s[:a] + s[a:b][::-1] + s[b:]
    else:
        s = s[:a] + p[0] + s[b:]

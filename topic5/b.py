while True:
    H, W = map(int, input().split())
    if H == 0 and W == 0:
        break
    for h in range(H):
        if h == 0 or h == H - 1:
            print("#" * W)
        else:
            print(f"#{'.'*(W - 2)}#")
    print()

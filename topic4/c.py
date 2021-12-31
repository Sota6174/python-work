while True:
    data = input()
    if '?' in data:
        break
    # eval：引数に文字列で入力した式を実行する
    print(eval(data.replace('/', '//')))

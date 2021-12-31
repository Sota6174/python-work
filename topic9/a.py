word = input().lower()
count = 0
while True:
    text = input()
    if text == "END_OF_TEXT":
        break
    count += text.lower().split().count(word)
print(count)

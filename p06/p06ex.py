num = int(input("1~100の数字を入力："))

f = open("hyaku.csv", "r", encoding="utf-8")
row = f.readlines()
f.close()

if 1 <= num <= len(row):
    data = row[num - 1].strip().split(",")

    author = data[0]
    top = data[1:4]
    bottom = data[4:6]

    print(author)
    for row in top:
        print(row)

    input("")

    for row in bottom:
        print(row)
else:
    print("無効な番号です。")
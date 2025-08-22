num = int(input("1~100の数値を入力："))

f = open("hyaku.csv", "r", encoding="utf-8")
row = f.readlines()
f.close()

if 1 <= num <= len(row):
    data = row[num - 1].strip().split(",")
    author = data[0]
    print(num,"は、",author,"の句です。")
else:
    print("無効な番号です。")
num = int(input("１～１０の番号を入力してください："))

f = open("fruits.csv", "r", encoding="utf-8")
row = f.readlines()
f.close()

if 1 <= num <= len(row):
    fruits = row[num - 1].strip()
    print(f"あなたには{fruits}")
    print(" をオススメします！")
else:
    print("無効な番号です。")
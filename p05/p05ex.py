numList = []
print("1から10の数字を3つ")
for i in range(3):
    num = int(input(f"{i+1}つ目："))
    numList.append(num)

f = open("fruits.csv", "r", encoding="utf-8")
row = f.readlines()
f.close()

recommendedSet = []
for num in numList:
    if 1 <= num <= len(row):
        fruits = row[num - 1].strip()
        recommendedSet.append(fruits)

print("あなたには",recommendedSet,"をオススメします！")
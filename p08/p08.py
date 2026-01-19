n = int(input("数を入力してください："))

s = 0  

for i in range(1, n + 1):
    s += i

print("1から", n, "までの合計は：", s)

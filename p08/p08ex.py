nL = int(input("小さい数値："))
nH = int(input("大きい数値："))

s = 0;

for i in range(nL, nH +1):
    s += i

print(nL, "から", nH, "までの合計は：", s)
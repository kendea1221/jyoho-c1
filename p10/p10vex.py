n = int(input("段数を入力してください："))

for i in range(1, n + 1):
    
    space = " " * (n - i)

    stars = "*" * (2 * i - 1)
    print(space + stars)
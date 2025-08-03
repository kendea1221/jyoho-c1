word = input("追加する文字を入力してください：")

file = open("text.txt", "a", encoding="utf-8")
file.write(word + "\n")
file.close()
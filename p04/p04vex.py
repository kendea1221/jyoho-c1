name = input("書き換えるファイル名を入力してください：")
fileName = name + ".txt"
msg = input("新しい内容を入力してください：")

f = open(fileName, "w", encoding="utf-8")
f.write(msg + "\n")
f.close()
name = input("ファイル名を入力してください：")
fileName = name + ".txt"

file = open(fileName, "w", encoding="utf-8")
file.close()
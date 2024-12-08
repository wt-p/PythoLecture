# mutable: 可変可能なオブジェクト list, dict, set
# fruits = ['apple', 'peach', 'banana']
# print(f"fruitsのIDは{id(fruits)}")
# fruits.append('lemon')
# print(fruits)
# print(f"fruitsのIDは{id(fruits)}")


# immutable: 変更不可能なオブジェクト int, float, str, bool, tuple
# fruit = 'apple'
# print(f"fruitのIDは{id(fruit)}")
# fruit += ', lemon'
# print(fruit)
# print(f"fruitのIDは{id(fruit)}")

# こちの方がtextに値入れるたびにメモリを使ってしまう
text = "" #1-2-3-4-5-6-7-...
for i in range(1, 11):
    if i == 1:
        text += str(i)
    else:
        text += '-' + str(i)
print(text)

# こちらの方はずっとlistが同じメモリ使う
text_list = []
for i in range(1, 11):
    text_list.append(str(i))

text = "-".join(text_list)
print(text)
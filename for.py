# forループ
fruits = ['apple', 'peach', 'grapes', 'banana']

# for fruit in fruits:
#     print(f"I love {fruit}!!")
#
# for char in  "hello world":
#     print(f"char: {char}")

# iterationとiterable

# challenge1
# favorite = input("好きなフルーツは？")
# for fruit in fruits:
#     if fruit == favorite:
#         print(f"{fruit}は好き")
#     else:
#         print(f"{fruit}は普通")

# challenge2
favorite = []
hate = []
for fruit in fruits:
    if input(f"{fruit}は好きですか？yes or no") == "yes":
        favorite.append(fruit)
    else:
        hate.append(fruit)
print(f"""
あなたの好きなフルーツリスト: {favorite}
あなたの嫌いなフルーツリスト: {hate}
""")
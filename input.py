# input(): ユーザの指定した値(文字列)を取得する

# age = input("何歳ですか？")
# print("あなたは{}歳です".format(age))

# challenge1
# age = int(input("何歳ですか？"))
# casino_age = 18
# if age >= casino_age:
#     print("Welcome!")
# else:
#     print("Get out!")

# challenge2
age = int(input("何歳ですか？"))
casino_age = 18
game_text = """プレイするゲームを選択してください
1: ルーレット
2: ブラックジャック
3: ポーカー
"""

if age >= casino_age:
    print("Welcome!")
    game = input(game_text)
    if game == '1':
        print("あなたはルーレットを選びました")
    elif game == '2':
        print("あなたはブラックジャックを選びました")
    elif game == '3':
        print("あなたはポーカーを選びました")
    else:
        print("1~3を選んでください")
else:
    print("Get out!")
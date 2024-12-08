casino_age = 18
game_dict = {'1': 'ルーレット', '2': 'ブラックジャック', '3': 'ポーカー'}

age = int(input("何歳ですか？"))
if age >= casino_age:
    print("Welcome!")
    while True:
        print("プレイするゲームを選択してください")
        for num, game_name in game_dict.items():
            print(f"{num}: {game_name}")
        game = input(":")
        if game in game_dict:
            print(f"あなたは{game_dict[game]}を選びました")
            break
        else:
            print("1~3を選んでください")
else:
    print("Get out!")

# 変数へ代入: assignment
hello = "konnnichiwa"
world = "sekai"
print(hello + world)
print("konnnichiwa" + "sekai")  # ハードコーディング

# format
print("{} {}".format(hello, world))
"hello {}".format("world")

name = "John"
print("Hey, {}!! How are you doing?".format(name))

balance = 100
print("balance: {}".format(balance))

# fstring
print(f"{hello} {world}")
print(f"Hey, {name}!! How are you doing?")
print(f"balance: {balance}")

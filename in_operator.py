# in演算子
fruits = ['apple', 'peach', 'grapes', 'banana']
print('lemon' in fruits)
print('lemon' not in fruits)
print('h' in 'hello')

# challenge
favorite_fruits = input("好きなフルーツは？")
if favorite_fruits in fruits:
    print("{}ですね、あげます".format(favorite_fruits))
    fruits.remove(favorite_fruits)
else:
    print("{}ですね、仕入れました！".format(favorite_fruits))
    fruits.append(favorite_fruits)
print("今あるフルーツはこちらです{}".format(fruits))

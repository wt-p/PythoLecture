# 数値型(Numeric): integer, float, complex

# int (integer, 整数）
print(type(1))

# float (浮動小数点)
print(type(0.1))
print(0.1 + 0.1 + 0.1) # 0.3ピッタリにならない

# Numeric Operator (数値演算子)
# 四則演算
print(1 + 0.4)
print(1 - 0.4)
print(2 * 3)
print(1 / 2)
print(5*6 - 3/6)

result = 1+ 1.0
print(f"type of result:{result} is {type(result)}")

#　その他の演算A
# floor division
print(14 // 3)
# modulo, 剰余,あまり
print(14 % 3)
# exponentiation 冪乗
print(2 ** 3)

hit_point = 100
attack_point = 40.3
remain = hit_point - attack_point
print(f"remain hit point is {remain}")

#augmented assignment +=, -=, *=, /=
a = 1
# a = a + 1
a += 1 # a = a + 1と同じ
print(a)
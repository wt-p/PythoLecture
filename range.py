# range(start, stop, step)
# for i in range(10):
#     print(i)
#
# for i in range(4, 13, 2):
#     print(i)
#
# for _ in range(3):
#     print("hello")

# challenge:FizzBuzz
for i in range(1, 51):
    if i % 15 ==  0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

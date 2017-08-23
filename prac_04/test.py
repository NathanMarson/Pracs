# text = "Enjoy the test"
# result = text.strip().split()[0]
# print(result)

# import math
# print(math.pi)

# def fn(x, y):
#     z = x + y
#     return z
#
# print(fn(1,2))

try:
    x = int("zero")
    print(10/x)
except ZeroDivisionError:
    print("div")

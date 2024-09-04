# lambda expression
# A lambda is an anonymous function that returns some form of data.

# def triple_me(num):
#     return num ** 3


o = lambda num: num * 3
print(o(10))

o = lambda num: num ** 3
print(o(10))


def add_10(n):
    return n + 10


o = lambda n: n + 10
print(o(100))


def mul(a, b):
    return a * b


oo = lambda a, b: a * b
print(oo(3, 4))

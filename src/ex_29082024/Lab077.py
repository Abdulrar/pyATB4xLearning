squares = [1, 4, 9, 16, 25]
print(squares)
print(squares.pop()) # supportsIndex -1
print(squares)

squares_t = ['test', 'list', 'Func', True, 11.3, 1100]
print(squares_t)
print(squares_t.pop())
print(squares_t)

print(squares_t.pop(-1))
print("list verify help --> ",squares_t)

print(squares_t.pop())
print(squares_t)

print("check positive index --> ",squares_t.pop(2))
print(squares_t)
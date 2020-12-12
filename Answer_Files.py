s = int(input())
squares = s ** 2
while s != 0:
    number = int(input())
    s += number
    squares += number ** 2
print(squares)

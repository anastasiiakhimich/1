max_ = 0
a = int(input())
b = 0
while a != 0:
    b = a + b
    a = int(input())
    if max_ < a:
        max_ = a
print('sum = ', b)
print()
print(max_)

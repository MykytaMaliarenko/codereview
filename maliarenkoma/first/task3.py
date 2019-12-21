"""
Вивести усі цілі числа із [a, b]
"""
a = float(input("a:"))
b = float(input("b:"))

for i in range(int(a), int(b) + 1):
    if i % 3 == 0 and a <= i <= b:
        print(i)

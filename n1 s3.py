n = int(input('введите число: '))
f = []
d = 2
while n > 1: 
    if n % d == 0:
        f.append(d)
        n = n // d
    else:
        d += 1
print(f)
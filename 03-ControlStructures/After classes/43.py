a, b = 0, 1
print(a, b, end=' ')

for _ in range(18):
    a, b = b, a + b
    print(b, end=' ')
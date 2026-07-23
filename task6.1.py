def countdown(n):
    while n >= 1:
        yield n
        n -= 1

for value in countdown(5):
    print(value)
def evens():
    n = 0
    while True:
        yield n
        n += 2

count = 0
for value in evens():
    print(value)
    count += 1
    if count == 5:
        break
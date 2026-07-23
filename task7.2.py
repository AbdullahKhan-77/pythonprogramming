def announce(func):
    def wrapper(*args, **kwargs):
        print("Calling...")
        result = func(*args, **kwargs)
        print("Done!")
        return result
    return wrapper

@announce
def add(a, b):
    return a + b

result = add(3, 5)
print(result)
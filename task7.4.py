def shout(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

@shout
def greet(name):
    return f"hello, {name}"

print(greet("ada"))


# shout wraps the greet function so when shout calls it greets the name ada and print hello ada inside the shout
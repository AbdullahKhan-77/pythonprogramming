def say_hi():
    print("hi")

def run_twice(func):
    func()
    func()

run_twice(say_hi)
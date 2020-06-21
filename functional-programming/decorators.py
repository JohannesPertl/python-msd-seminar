# Decorator design pattern

def do_twice(func):
    def wrapper():
        func()
        func()

    return wrapper

@do_twice
def hello_world():
    print("Hello world!")


# hello_world = do_twice(hello_world)

hello_world()


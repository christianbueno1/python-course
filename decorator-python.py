def succ(function):
    def wrapper(*args, **kwargs):
        return function(*args, **kwargs) + 1

    return wrapper

@succ
def add(x, y):
    return x + y

print(add(1, 2))

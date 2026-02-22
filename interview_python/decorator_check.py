def decorator(func):
    def wrapper():
        print('hello')
        func()
        print("completed")
    return wrapper

@decorator
def greet():
    print('hi')

greet()
#decorator is a function that takes another function as an argument and returns a function
def decorator(func):
    def wrapper():
        print("Tranaction Initiated")
        func()
        print("Tranaction Completed")
    return wrapper


@decorator
def hello():
    print("....Executing all steps of Transaction..")


hello()
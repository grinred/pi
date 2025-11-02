import Myenum as bs


class Dec:
    def my_decorator(func):
        def wrapper():
            print("Something happens before the function is called.")
            func()
            print("Something happens after the function is called.")

        return wrapper


@Dec.my_decorator
def say_hello():
    print("HIHI")


say_hello()

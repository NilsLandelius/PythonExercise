def decorator_with_arguments(function):
    def wrapper_accepting_arguments(arg1, arg2):
        print("My arguments are: {0}, {1}".format(arg1,arg2))
        function(arg1, arg2)
    return wrapper_accepting_arguments


@decorator_with_arguments
def cities(city_one, city_two):
    print("Cities I love are {0} and {1}".format(city_one, city_two))

#cities("Nairobi", "Accra")


def uppercase_decorator(function):
    def wrapper():
        print('uppercase')
        func = function()
        make_uppercase = func.upper()
        print('uppercase end')
        return make_uppercase

    return wrapper


def split_string(function):
    def wrapper():
        print('split string')
        func = function()
        splitted_string = func.split()
        print('split end')
        return splitted_string

    return wrapper

@split_string
@uppercase_decorator
def say_hi():
    print('say hi')
    return 'hello there'

print(say_hi())
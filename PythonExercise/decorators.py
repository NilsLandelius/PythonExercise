#Decorators are functions called before other functions.
#Ex: @Classmethod , @StaticMethod

import functools
#--------In this example, the functool is used to wrap the method "my_decorator" 
#--------As the @my_decorator is called, the method "my_function" is passed to
#--------my_decorator() -> function_that_runs_func(). That method runs the passed
#--------method, in this case "my_function" but also runs some code before and after
#--------This demonstrates how the decorators are run before it's associated method
def my_decorator(func):
    @functools.wraps(func)
    def function_that_runs_func():
        print("In the decorator!")
        func()
        print("After the decorator!")
    return function_that_runs_func

@my_decorator
def my_function():
    print("I'm the function!")


#my_function()

#----A good usecase for decorators with arguments could be when you
#----pass user privilages, if the rights are not at a high enough level
#----then we will run some other code. With a deocrator the call to 
#----check user privilages becomes a lot easier.
def decorator_with_arguments(number):
    def my_decorator(func):
        @functools.wraps(func)
        def functions_that_runs_func(*args,**kwargs): #always use args and kwargs in decorators because they can be applied to any method with unknown arguments
            print("In the decorator!")
            if number == 56:
                print("not running function")
            else:
                    func(*args,**kwargs) #always use args and kwargs in decorators because they can be applied to any method with unknown arguments
            print("After the decorator!")
        return functions_that_runs_func
    return my_decorator

@decorator_with_arguments(42)
def my_function_too(arg1,arg2):
    print("Hello {}, your argument is {}".format(arg1,arg2))

my_function_too("Nils",arg2 = "null") 



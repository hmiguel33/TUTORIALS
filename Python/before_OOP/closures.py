# CLOSURES

# They allows us to take advantage of first-class functions, and returns an inner function that remembers
# and has access to variables local to the scope in which they were created

# a closure is an inner funciont that remembers and has access to variables on the local scope
# on which it was created, even after the outer_function has finished executing

#############################################################
#            BASIC EXAMPLE                                  #
# refer to First_class_functions.py to understand better    #
#############################################################


# def outer_func():
#     message='Hi!'
#     def inner_func():
#         print(message)      # the variable message WAS NOT created on the inner function,
                              # but it has access to it, message is what is called a "FREE VARIABLE"

#     return inner_func

# my_func = outer_func()   # looks like does nothing, but actually my_func=inner_func, because is the return value of outer_func
# my_func()               # executes inner_func




#############################################################
#              example passing parameters                   #
#############################################################

def outer_func(msg):
    message=msg
    def inner_func():
        print(message)

    return inner_func

hi_func = outer_func('Hi!')
hello_func = outer_func('Hello!')

hi_func()

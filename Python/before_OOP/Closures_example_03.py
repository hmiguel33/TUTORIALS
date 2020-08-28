# Closures example
import logging
logging.basicConfig(filename='example.log',level=logging.INFO)

def logger(func):
    def log_func(*args):                                                            #  takes any number of arguments, it is what *args means
        logging.info('Running "{}" with arguments {} '.format(func.__name__, args))  # we are logging the functiont that we passed in, with the arguments
        print(func(*args))                     # we execute the function we passed with the arguments and we print that to the console
    return log_func                            # we return inner log_func


def add(x,y):
    return x+y

def substract(x,y):
    return x-y


add_logger = logger(add)
add_logger(3,5)

subs_logger= logger(substract)
subs_logger(3,5)


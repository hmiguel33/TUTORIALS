# Decorators_example
from functools import wraps

def my_logger(original_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(original_func.__name__), level=logging.INFO)    

    @wraps(original_func)
    def wrapper(*args,**kwargs):
        logging.info('Ran with args: {} and kwargs {}'.format(args,kwargs))
        return original_func(*args,**kwargs)

    return wrapper


def my_timer(original_func):
    import time


    @wraps(original_func)
    def wrapper(*args,**kwargs):
        t1=time.time()
        result = original_func(*args,**kwargs)
        t2= time.time()-t1
        print('{} ran in {} seconds'.format(original_func.__name__,t2))
        return result

    return wrapper

# @my_logger
# def display():
#     print('display function ran')

import time

@my_logger
@my_timer
def display_info(name,age):                         
    time.sleep(1)
    print('display info ran with arguments {} and {}'.format(name,age))


display_info('Thomas',38)


# display_info=my_logger(display_info)


# print(display_info.__name__)
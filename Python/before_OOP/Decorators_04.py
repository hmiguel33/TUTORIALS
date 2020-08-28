# DECORATORS

# are functions that take another function as an argument adds some functionality and returns another function,
# without modifying the source code of function that was passed-in

# def decorator_func(original_func):                # "decorator_func" function, receives a function as an argument 
# 						    # we declare that as a variable original_func

# 	def wrapper_func():                         # "wrapper_func" is a function inside "decorator_func"
# 		print('wrapper executed this before {}'.format(original_func.__name__))
# 		return original_func()              # returns "original_func()" and executes it

# 	return wrapper_func  			    # We return the inner function "wrapper_func" without executing it 


# def display():
# 	print('display function ran')


# decorated_display=decorator_func(display)   # we are creating a variable "decorated_display" which is equal
# 						# to our "decorator_func" function, and we are passing our
# 						# "display" function as an argument so at this point 
# 						# "decorated_display = wrapper_func"


# decorated_display()				# as "decorated_display = wrapper_func" then, decorated_display()
# 						# is equivalent to  "wrapper_func()"

############################################################################################
#
# in line 19, we assign a function to a variable and pass a function as an argument
#
#						decorated_display=decorator_func(display)	
#
# after execution we receive as a result the function inside the argument function.
# Then we execute the inner function, sinside the function we passed as an argument
# 
#						decorated_display()
#
#This is equivalent to:
#
#			@decorator_func    <--- This is how you normally see decorators
#				def display():
#					print('display function ran')
#						
# The lines:
#			@decorator_func    
#				def display():
#
# are equivalent to:
#		
#			display = decorator_func(display)
#
# meaning: display function, is equal to "decorator_function", that takes display function
#          as an argument.
#
# Note: We changed "decorated_display" variable for the function name as variable "display"
############################################################################################
#
#					REWRITING AFTER DISPLAY FUNCTION
#
############################################################################################

# @decorator_func
# def display():
# 	print('display function ran')

# display()

############################################################################################
#					comment everything above
#					multiple functions using the same decorator
############################################################################################

# def decorator_func(original_func):                  # "decorator_func" function, receives a function as an argument 
# 						      # we declare that as a variable original_func

# 	def wrapper_func(*args,**kwargs):             # "wrapper_func" is a function inside "decorator_func"
# 		print('wrapper executed this before {}'.format(original_func.__name__))
# 		return original_func(*args, **kwargs)  # returns "original_func()" and executes it

# 	return wrapper_func  				


# @decorator_func
# def display():
# 	print('display function ran')

# @decorator_func
# def display_info(name,age):							# new function display info, receives two arguments name and age
# 	print('display info ran with arguments {} and {}'.format(name,age))


# display_info('George',35)							# To test the new function with our decorator function
# 										# we need to add *args and **kwargs to accept any number
# 										# of argument and/or keywords in our wrapper function.


############################################################################################
#						CLASS AS DECORATOR  (comment the previous code)
# 		  			   instead of functions
############################################################################################

# def decorator_func(original_func):                  # "decorator_func" function, receives a function as an argument 
# 						      # we declare that as a variable original_func

# 	def wrapper_func(*args,**kwargs):             # "wrapper_func" is a function inside "decorator_func"
# 		print('wrapper executed this before {}'.format(original_func.__name__))
# 		return original_func(*args, **kwargs)                          # returns "original_func()" and executes it

# 	return wrapper_func  				


class decorator_Class(object):
  	def __init__(self, original_func):
		self.original_func = original_func

	def __call__(self, *args,**kwargs):
		print('__call__ method executed this before {}'.format(self.original_func.__name__))
		return self.original_func(*args, **kwargs)                          # returns "original_func()" and executes it


@decorator_Class
def display():
	print('display function ran')

@decorator_Class
def display_info(name,age):							# new function display info, receives two arguments name and age
	print('display info ran with arguments {} and {}'.format(name,age))


display_info('George',35)							# To test the new function with our decorator function
										# we need to add *args and **kwargs to accept any number
										# of argument and/or keywords in our wrapper function.


display()

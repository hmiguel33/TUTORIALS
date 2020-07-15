# First class functions

# A programing Language has First Class functions, if it treats funtions as first-class citizens.

# A "first-class" citizen in programming
# Is an entity that supports all operations generally available to other entities. 
# These include:
#   - Tipically being passed as an argument.
#   - Returned from a function.
#   - Assigned to a variable.


#############################################################################
#               functions used trought he whole exersice                    #
#                       Do not comment!!!!!                                 #
#############################################################################

def square(x):          # Function square
    return x*x


def cube(x):            # Function cube
    return x*x*x


#############################################################################
#                       SECTION                                             #
#               ASSIGN A FUNCTION TO A VARIABLE                             #
#  comment and/or uncomment this part as you go reach a new section         #
#############################################################################

# f= square(5)            # function "square" receives the value "5" and is assigned to variable f
# print(square)           # we are printing the function "square" - result= prints it is a function called square and the address where it is located
# print(f)                # we are printing "f" which has asigned the function with is execution where we assigned the value of 5 - Result= provides the result of the execution of the function


#######  We can change the definition of f as:
#######                  f = square             # Note: without parentheses!!!
####### ( for clarity comment lines 16,17,18)

# f= square               # Note: without parentheses!!!
# print(square)           # we are printing the function "square" - result= prints it is a function called square and the address where it is located
# print(f)                # we are printing the function "square" trough f - result= prints it is a function called square and the address where it is located

# print(f(5))             # I can execute the function trough f, because it was asigned on line 28. this will return 25.


#############################################################################
#                       SECTION                                             #
#                                                                           #
#   "WE CAN PASS FUNCTIONS AS ARGUMENTS AND RETURN FUNCTIONS AS RESULTS"    #
#                                                                           #
#              Functions with that hability are called                      #
#                                                                           #
#                     HIGER-ORDER FUNCTIONS                                 #
#############################################################################
#############################################################################
#               PASSING A FUNCTION AS ARGUMENT                              #
#############################################################################

# def my_map(func, arg_list):             # function "my_map" receives a fucntion and a vector 
#     result =[]                          # declares an empty vector called "result"
#     for i in arg_list:                  # iteratates troug the vector that was passed to the function
#         result.append(func(i))          # appends result of function square of the ith element of the vector that was passed 
#     return result                       # returns vector called "result"
 
# squares=my_map(square,[1,2,3,4,5])      # we are passing function "square" without parentheses and an array to function "my_map", adding parentheses will try to execute the function and we do not want that.

# print(squares)

# cubes=my_map(cube,[1,2,3,4,5])

# print(cubes)


#############################################################################
#               RETURN A FUNCTION FROM ANOTHER FUNCTION                     #
#############################################################################


def logger(msg):                # Function logger, receives "msg" as an argument
    def log_message():          # Function log_message does not receive anything 
        print('Log :', msg)     #   but prints Log: "whatever content of message" 

    return log_message          # function logger returns function "log_message" without parentheses
                                # because we do not want to execute the function "log_message" at this point

log_hi= logger('Hi!')           # "log_hi" is assigned the result of function logger, because we used parentheses and passed an argument
                                # the result is log_hi = log_message, since it is the return value of logger, nothing has been printed at this point. 
                                # now we can treat log_hi as log_message, which takes no arguments.

log_hi()                        # log_hi = log_message and the parentheses executes "log_message" printing 'Log :', 'Hi!',  it remembers the message "msg" we passed to logger

########
######## the operation performed by the last 2 lines  of code is called a CLOSURE
########

#######  EXAMPLE
#######

def html_tag(tag):                                  # Function logger, TAKES AS AN ARGUMENT "tag" 
    def wrap_text(msg):                             # Function wrap_text, inside of html_tag, TAKES AS AN ARGUMENT "msg" 
        print('<{0}><{1}></{0}>'.format(tag,msg))   # When you execute wrap_text prints (tag, message, tag) a 
    return wrap_text                                # Function html_tag returns wrapt_text function without parentheses

print_h1= html_tag('h1')                            # print_h1 variable calls "html_tag" passing 'h1' as argument i.e. print_h1 = wrap_text (nothing has been printed yet)
print(print_h1)                                     # Here you can see that "print_h1" is equal to function wrap_text, waiting to be executed
print_h1('This is a headline')                      # print_h1 acts as wrap_text and passes 'This is a headline' as message or msg and it remembers the tag we passed to html_tag
print_h1('This is another headline')                # print_h1 acts as wrap_text and passes 'This is another headline' as message or msg


print_p = html_tag('p')
print_p('This is a paragraph')
print_p('This is another paragraph')




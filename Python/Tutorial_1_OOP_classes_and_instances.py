class Student:
    def __init__(self, name, last,age ):   #<-- the method __init__ can be seen as the "constructor" of the class
                                           #     it is called everytime we create an instance or object.
                                           # -----------------------------------------------------
        self.name=name                     # <-- Instance variables are owned by instances of the class. 
        self.last=last                     #     This means that for each object or instance of a class, the values of instance variables are different.
        self.age=age
        self.email = name + '.' +last + '@school.com'

    def fullname(self):                     
        return '{} {}'.format(self.name, self.last)



std_1= Student('miguel','smith',23)         # <-- std_1 is an instance of the class Student
std_2= Student('stefan', 'van der dutch',25) # <-- std_2 is an instance of the class Student

# print(std_1.fullname())         # <-- we can access the methods of the class trough an instance and print the full name of a student
# std_1.fullname()                # <-- we acces the method fullname() of the instance std_1, the parentheses execute the method.
print(Student.fullname(std_1 ))   # <-- We can access the method fullname() trough the class name. This is equivalent to the previous line
                                  

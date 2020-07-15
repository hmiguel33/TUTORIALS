# polymorfism
#############################################
#Polymorphism with Function and Objects
#############################################
# You can create a function that can take any object, allowing for polymorphism.

# Let’s take an example and create a function called “func()” which will take an object which we will name “obj”. 
# Now, let’s give the function something to do that uses the ‘obj’ object we passed to it. 
# In this case, let’s call the methods type() and color(), each of which is defined in the two classes ‘Tomato’ and ‘Apple’. 
# Now, you have to create instantiations of both the ‘Tomato’ and ‘Apple’ classes if we don’t have them already


class Tomato(): 
	 def type(self): 
	   print("Vegetable") 
	 def color(self):
	   print("Red") 

class Apple(): 
	 def type(self): 
	   print("Fruit") 
	 def color(self): 
	   print("Red") 
	  
def func(obj): 
	   obj.type() 
	   obj.color()
		
obj_tomato = Tomato() 
obj_apple = Apple() 
func(obj_tomato) 
func(obj_apple)


#############################################
#Polymorphism with Class Methods
# #############################################

# Python uses two different class types in the same way. 
# Here, you have to create a for loop that iterates through a tuple of objects.
# Next, you have to call the methods without being concerned about which class type each object is. 
# We assume that these methods actually exist in each class.

# Here is an example to show polymorphism with class:


class India():
	def capital(self):
		print("New Delhi")
 
	def language(self):
		print("Hindi and English")
 
class USA():
	def capital(self):
		print("Washington, D.C.")
 
	def language(self):
		print("English")
 
obj_ind = India()
obj_usa = USA()

for country in (obj_ind, obj_usa):
	country.capital()
	country.language()


#############################################
#Polymorphism with Inheritance
#############################################

# Polymorphism in python defines methods in the child class that have the same name as the methods in the parent class. 
# In inheritance, the child class inherits the methods from the parent class. 
# Also, it is possible to modify a method in a child class that it has inherited from the parent class.

# This is mostly used in cases where the method inherited from the parent class doesn’t fit the child class. 
# This process of re-implementing a method in the child class is known as Method Overriding.

class Bird:
	def intro(self):
		print("There are different types of birds")
 
	def flight(self):
		print("Most of the birds can fly but some cannot")
 
class parrot(Bird):
	def flight(self):
		print("Parrots can fly")
 
class penguin(Bird):
	def flight(self):
		print("Penguins do not fly")
 
obj_bird = Bird()
obj_parr = parrot()
obj_peng = penguin()
 
obj_bird.intro()
obj_bird.flight()
 
obj_parr.intro()
obj_parr.flight()
 
obj_peng.intro()
obj_peng.flight()


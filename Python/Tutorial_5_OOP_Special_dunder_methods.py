# Dunder methods or magic methods 
# This is how we implement operator overloading
# with these methods we can change some built-in behavior and operations
# They are always surrounder by double underscores "__method__()"
# Example: __init__():

class Client:

	discount = 0.04              # <-- class variable
	num_clients=0                # <-- class variable

	def __init__(self, name, last,price ):   
		self.name=name
		self.last=last
		self.price=price
		self.email = name + '.' +last + '@client.com'

		Client.num_clients+=1    

	def fullname(self):                                 # regular method 
		return '{} {}'.format(self.name, self.last)


	def total_discount(self):                           # regular method
		self.price = int(self.price - self.price * self.discount) 

								  # this funcion already exist in our class, however we can adapt our own as a fall-back
	def __repr__(self):           # an unambiaguous representation of the object, should be used for debugging, logging etc, really meant to be seen by other developers
		return "Client('{}','{}', {})".format(self.name, self.last,self.price)

	def __str__(self):            # a readable representation of an object, meant to be as a display to the end-user
		return '{} - {}'.format(self.fullname(), self.email) 

	def __add__(self,other):
		return self.price + other.price

	def __len__(self):
		return len(self.fullname())


cl_1= Client('tom','sawyer',4000 )                   # creation of instances
cl_2= Client('stefan', 'van der dutch',250)            # creation of instances


# print(cl_1)
print(repr(cl_1))
print(str(cl_1))

print(cl_1+cl_2)					# it uses the __add__ method in our class and performs the sym of the "price" for 2 clients
print(len(cl_1))					# it uses the __len__ method that we modified in our class.



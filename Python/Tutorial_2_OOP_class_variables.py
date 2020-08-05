#class variables :are defined within the class construction. Because they are owned by the class itself, they are shared among all instances of a class

class Client:

    discount = 0.04;     # <-- class variable
    num_clients=0;       # <-- class variable

    def __init__(self, name, last,price ):   
        self.name=name
        self.last=last
        self.price=price
        self.email = name + '.' +last + '@client.com'

        Client.num_clients+=1      #<-- This variable class gives us the number of clients, or the number of instances in the class.
                                   #<-- Is more useful here, since the __init__ method is called every time when an instance is created.
                                   #    It is not necessaryto use self, only the class Name, it won't make sense to use self.

    def fullname(self):
        return '{} {}'.format(self.name, self.last)


    def total_discount(self):
        self.price = int(self.price - self.price * self.discount) # <--class variable "discount", can be used with the instance "self" or the Class Client, but never alone
                                                                  # Important. Self allows us to modify the value for an instance,




std_1= Client('mike','wolf',4000 )                   # creation of instances
std_2= Client('stefan', 'van der dutch',250)            # creation of instances

# print(std_1.__dict__)             # __dict__ shows the attributes of the instance std1
# print(Client.__dict__)            # shows shows the attributes of the class, class variables and methods

Client.discount = 0.05              # modifies Class variable "discount" for all instances

# std_1.discount =0.5               # modifies Clas variable "discount" ONLY for std_1 instance
# print(std_1.__dict__)             # prints instance variables, shows values of instance variables std_1 and the modified value of the variable "discount" for std_1
# print(std_2.__dict__)             # prints instance variables, shows values of instance variables std_2

print(Client.discount)              # calls class variable "discount" and prints it on screen
print(std_1.discount)               # calls class variable "discount" trough instance std_1 and shows it's value on the screen
print(std_1.price)                  # calls instance variable "price" trough instance std_1 and shows it's value on the screen
std_1.total_discount()              # calls and execute method total_discount() with instance std_1.
print(std_1.price)                  # calls and shows instance variable "price" trough instance std_1, which has been modified on previous line
print(std_2.discount)               # calls class variable "discount" trough std_2 instance.

# # std_2.total_discount()          # calls and execute method total_discount() with instance std_2.
# # print(std_2.price)              # calls instance variable "price" trough instance std_2 and shows it's value on the screen

# print(Client.num_clients)         # Calls class variable "num_clients" and shows it's value on the screen 


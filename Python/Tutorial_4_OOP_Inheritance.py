# INHERITANCE and subclases 
# Let's create clients by department, kitchen and men clothes.




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



class Kitchen(Client):
    discount = 0.30
    
    def __init__(self, name, last,price, pgr_lan ): # the init method of the child class creates a constructor, using the same arguments of the base clase
                                                    # However, on the next line, we will allow the base class to handle the arguments it already initializes.

        super().__init__(name, last,price)          # This line is better because is more maintainable, specially for multiple inheritance, then is necessary
        #Client.__init__(self, name, last,price)    # These two lines do exactly the same, this works good for single inheritance
        self.pgr_lan = pgr_lan                      # This is a variable member of the child class.




class Manager(Client):

    def __init__(self, name, last,price, clients=None):
        super().__init__(name, last,price) 
        if clients is None:
            self.clients = []
        else :
            self.clients=clients

    def add_cli(self, cli):
        if cli not in self.clients:
            self.clients.append(cli)

    def rem_cli(self, cli):
        if cli in self.clients:
            self.clients.remove(cli)

    def print_clients(self):
        for cli in self.clients:
            print('==>', cli.fullname())



# cl_1= Client('tom','sawyer',4000 )                   # creation of instances
# cl_2= Client('stefan', 'van der dutch',250)            # creation of instances

# print(cl_1.email)
# print(cl_2.email)

################################################################
# Now we create two instances of the child class Kitchen (hast no constructor this class )
#
# Kitchen has no __init__method, so Python will walk the chain on inheritance, until it finds the __init__ method.
# that chain is called the METHOD RESOLUTION ORDER
################################################################


cl_K_1= Kitchen('tom_kitchen','sawyer',4000, 'python')                   # creation of instances
cl_K_2= Kitchen('stefan_Kitchen', 'van der dutch',250,'c++')            # creation of instances

print(cl_K_1.price)
cl_K_1.total_discount() 
print(cl_K_1.price)

print(cl_K_2.pgr_lan)


mgr1 = Manager('will', 'smith', 50000 , [cl_K_1] )

print(mgr1.email)

mgr1.add_cli(cl_K_2)


mgr1.print_clients()

mgr1.rem_cli(cl_K_1)

mgr1.print_clients()


print(isinstance(mgr1,Manager) )         # we can check if one of our instances is inatence of our class or not
print(isinstance(mgr1,Client) )
print(isinstance(mgr1,Kitchen) )


print(issubclass(Kitchen, Client))
print(issubclass(Kitchen, Manager))


# print(help(Kitchen))                                          # This allows you to see in the console, the resolution order in the console, methods inherited, data descriptors and attributes inherited from the base class.


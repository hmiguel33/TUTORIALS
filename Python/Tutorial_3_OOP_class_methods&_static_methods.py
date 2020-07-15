# - Regular Methods in a class, automatically take the instance as the first argument, called "self".
# - Class Methods, automatically pass the class as the first argument, and is called  "cls"
# - Static Methods, don't pass anything automatically. They  behave as a regular function
#   but are included in the class, because they hace some logical connection with it.
#   Static Methods, don't operate on the instance or the class


class Client:

    discount = 0.04;              # <-- class variable
    num_clients=0;                # <-- class variable

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


    @classmethod                                        #class method 
    def set_discount_amt(cls, amount):
        cls.discount = amount

    @classmethod                                        #class method  - as alternative constructor  -
    def from_string(cls,cl_str):
        name, lastname, price= cl_str.split('-')
        return cls(name,lastname,price)


    @staticmethod
    def is_workday(day):
        # in python, by convention Monday = 0 and Sunday =6
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        else:
            return True


std_1= Client('tom','sawyer',4000 )                   # creation of instances
std_2= Client('stefan', 'van der dutch',250)            # creation of instances



#################################################
#               REGULAR methods               #
#################################################



# print(Client.discount) 
# print(std_1.discount) 
# print(std_2.discount) 

#################################################
#               CLASS methods               #
#################################################
#Client.set_discount_amt(0.05)
# print(Client.discount) 
# print(std_1.discount) 
# print(std_2.discount) 



# client_1= 'Mike-Franz-2000'
# client_2= 'John-Stuart-100'
# client_3= 'Barak-Obama-5000'

# name, lastname, price= client_1.split('-')

# client1= Client.from_string(client_1)
# print(client1.name)
# print(client1.last)
# print(client1.price)
# print(client1.email)


#################################################
#               STATIC methods               #
#################################################


import datetime

mydate= datetime.date(2020, 7, 15)

print(Client.is_workday(mydate))
# Property Decorators - Getters, Setters, and Deleters
# PROBLEM: we made a mistake on the name of our client, how do we automaticaly cahnge mail and fullname?
# The property decorator allows to acces a method, this allows to define a method but we can access it as an attribute.

class Client:

    def __init__(self, name, last ):   
        self.name=name
        self.last=last
     
        #self.email = name + '.' +last + '@client.com'                 # <-- DEPENDS ON NAME AND LAST variables

    @property
    def email(self):                                 # regular method 
        return '{}.{}@client.com'.format(self.name, self.last)


    @property
    def fullname(self):                                 # regular method 
        return '{} {}'.format(self.name, self.last)

    @fullname.setter
    def fullname(self,fname):
        name, last= fname.split(' ')
        self.name= name
        self.last= last

    @fullname.deleter
    def fullname(self):
        print('Delete Name')
        self.name=None
        self.last=None





cl_1= Client('tom','wall')                   # creation of instances

                                
                               
cl_1.name="peter"              # change name of client, but doesnt change for the email, it will still give me tom, instead of peter

cl_1.fullname="mike walsh"


print(cl_1.name)
print(cl_1.email)               # this can't change the name, because will take the values given by the instance
print(cl_1.fullname)          # this changes the name, because the method takes the current value of the instance

del(cl_1.fullname)
# # students = [
# #     'nat',
# #     'joe',
# #     'mark'
# # ]

# # students.append('Steven')

# # append(students, 'Steven')

# # def append(name):
    

# # OOP == create your own datatype or CLASS
# # method is a function tied to a specific dataype

# # class Contact(object):
# #     def __init__(self, first, middle, last, number):
# #         self.first_name = first
# #         self.middle_name = middle
# #         self.last_name = last
# #         self.number = number
# def get_attr(obj, attr):
#     if attr in obj.attributes:
#         return obj.attributes[attr]
#     else: 
#         return ''

# class Contact(object):
#     def __init__(self, params):
#         # self.first_name = params['first']
#         # self.middle_name = params['middle']
#         # self.last_name = params['last']
#         # self.number = params['number']
#         self.attributes = params
    
#     def first_name(self):
#         return self.get_attr('first')
    
#     def middle_name(self):
#         return self.get_attr('middle')
            
#     def last_name(self):
#         return self.get_attr('last')

#     def number(self):
#         return self.get_attr('number')

#     def get_attr(self, attr):
#         if attr in self.attributes:
#             return self.attributes[attr]
#         else: 
#             return ''

#     def as_string(self):
#         return '%s %s %s: %s' % (self.first_name(), self.middle_name(), self.last_name(), self.number())

# # jon = Contact('Jonathan', 'Lee', 'Martin', 67382002)
# jon = Contact({'first': 'Jonathan', 'middle': 'Lee', 'last': 'Martin', 'number': 67382002})


# class Phonebook(object):
#     # stores list of Contacts (objects!)
#     def __init__(self):
#         self.contacts = []
    
#     def add(self, contact):
#         self.contacts.append(contact)

#     def as_string(self):
#         string = ''
#         for contact in self.contacts:
#             string += contact.as_string() + '\n'
        
#         return string


#     # def remove():
#     #     ...

#     # def sort():
#     #     ...

#     # def lookup_by_name():
#     #     ...
    
#     # def lookup_by_email():

# phonebook = Phonebook()

# jon = Contact({'first': 'Jonathan','middle': 'Lee', 'last': 'Martin', 'number': 67382002})

# phonebook.add(jon)

# print phonebook.as_string




## Defines and calls Person class:

# class Person(object):
#     def __init__(self, params):
#         self.name = params['name']
#         self.email = params['email']
#         self.phone = params['phone']

#     def greet(self, other_person):
#         return 'Hello %s, I am %s!' % (other_person.name, self.name)

# sonny = Person({'name': 'Sonny', 'email': 'sonny@hotmail.com', 'phone': '344-234-9821'})
# jordan = Person({'name': 'Jordan', 'email': 'jordan@aol.com', 'phone': '430-222-2910'})


# print sonny.greet(jordan)
# print jordan.greet(sonny)
# print '%s: %s, %s' % (sonny.name, sonny.email, sonny.phone)
# print '%s: %s, %s' % (jordan.name, jordan.email, jordan.phone)



class Vehicle(object):
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def print_info(self):
        print '%s %s %s' % (self.year, self.make, self.model)

car = Vehicle('Nissan', 'Leaf', 2015)
print car.make
print car.model
car.print_info()


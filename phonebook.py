phonebook_dict = {}

def new():
   name = raw_input('Name: ')
   number = raw_input('Phone Number: ')
   phonebook_dict[name] = number
   print 'Entry stored for ' + name

def lookup():
   name = raw_input('Name: ')
   if name in phonebook_dict:
       print 'Found entry for ' + name + ': ' + phonebook_dict[name]
   else:
        print 'Not found.'

def delete():
   name = raw_input('Name: ')
   del phonebook_dict[name]
   print 'Deleted entry for ' + name
   return phonebook

def show():
    show_all = ''
    for each in phonebook_dict.items():
       entry = 'Found entry for ' + each[1] + ': ' + each[0] + '\n'
       show_all += entry
    print show_all

def phonebook():
    questions =  "\nElectronic Phone Book \n===================== \n1. Look up an entry \n2. Set an entry \n3. Delete an entry \n4. List all entries \n5. Quit\n"
    
    answer = 0

    while answer != 5:
        print questions
        answer = input('What do you want to do? (1-5): ')

        if answer == 1:
            lookup()
        elif answer == 2:
            new()
        elif answer == 3:
            delete()
        elif answer == 4:
            show()
        elif answer == 5:
            return 'Bye.'
        else:
            return 'Try again.'
    
phonebook()


# phonebook = {

# }

# keep_running = True
# while keep_running:
#     keep_running = run_phonebook()



# def run_phonebook():
#     print menu
#     number = raw_input
#     if number in menu_options:
#         menu_option = men_options[number]
#         print menu_option
#     else:
#         'Invalid. Try again'
#     return number != 5


# menu_options = {
#     '1': function,
#     ...
# }



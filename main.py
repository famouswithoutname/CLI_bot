phone_numbers = {}

def close_bot():
    
            print("Good bye!")
            return False

def check(input):
     check_command = input.split(' ')
     if check_command[0].lower() == 'add':
          for key in phone_numbers:
               if check_command[1] == key:
                    print("Contact already exist!")
                    return False
               else:
                    continue
     elif check_command[0].lower() == 'change' or check_command[0].lower() == 'phone':
          count = False
          for key in phone_numbers:
               if check_command[1] == key:
                    count = True
                    continue
          if count == False:
               print('Contact does not exist')
               return count     
     return True               
                    



def add(input):
    contact = input.split(' ')
    if contact[0] == 'add':
        
        contact.remove(contact[0])
        phone_numbers[contact[0]] = contact[1]
        print("Add new succecful")
        print(phone_numbers)
        return True
    

def change(input):
     contact = input.split(' ')
     if contact[0] == 'change':
          contact.remove(contact[0])
          phone_numbers[contact[0]] = contact[1]
          print(f'Change {contact[0]} succecful')
          return True
     
def phone(input):
     contact = input.split(' ')
     if contact[0] == 'phone':
          contact.remove(contact[0])
          print(f'Phone number of {contact[0]} is {phone_numbers[contact[0]]}')
          return True

def main():
    question = True
    while question == True:
        
        print("Hello\n It's your helper.\n You can use second command:\n1.hello\n2.add ...\n3.change ...\n4.phone ...\n5.show all\n6.good bye|close|exit")
        
        word = input("Write a comand: ")
        command = word.split()
        
        if len(command) == 0:
             print('You need write something!')
             continue
        elif len(command) == 1:
             command.append(' ')
        
        if word.lower() == 'close' or word.lower() == 'good bye' or word.lower() == 'exit':
            question = close_bot()
        elif command[0].lower() == 'add':
             if check(word):
               question == add(word)
             else:
                  continue  
        elif command[0].lower() == 'change':
             if check(word):
               question = change(word)
             else:
                  continue  
        elif command[0].lower() == "phone":
               if check(word):
                    question = phone(word)
               else:
                    continue
        elif command[0].lower() + ' ' + command[1].lower() == 'show all':
             print(phone_numbers)
             question = True
        elif command[0].lower == 'hello':
             print('How can I help you?')
        else:
             print('You write wrong command, please try again and write in the next format:\nCommand Name Phone')
             continue
             
             

main()

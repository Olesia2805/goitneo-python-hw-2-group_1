def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (ValueError, KeyError, IndexError) as e:
            return str(e)

    return inner

def parse_input(user_input):
    """The function takes a string of user input, breaks it into words.
It returns the first word as the command cmd and the rest as a list of arguments *args.
Next, it removes extra spaces around the command and converts it to lower case."""
    command, *args = user_input.split()
    command = command.strip().lower()
    return command, *args

@input_error
def add_contact(args, contacts):
    """this add-function has to have 2 args (name and phone (int number))
which it will use for adding to the list"""
    
    name, phone = args
    
    if phone is not phone.isdigit() and len(phone) < 10:
        raise ValueError ("Second argument need to be phone number")
    
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    """this change-function has to have 2 args (name and phone (int number))
which it will use for changing the user's phone to the list"""
    if len(args) < 2:
        raise ValueError("Please provide both name and phone")
    
    name, phone = args
    
    if name not in contacts:
        raise ValueError ("Second argument need to be phone number")
    
    if phone is not phone.isdigit():
        raise KeyError (f"I don't find {name} in list")            
    
    contacts[name] = phone
    return "Contact updated."
        
                          
@input_error
def show_phone(args, contacts):
    """this function show someone's phone number (if it is possible)"""
    if len(args) == 1:
        name = args[0]
        if name in contacts:
            return contacts[name]
        else:
            raise ValueError (f"I don't find {name} in list")
    else:
        raise IndexError ("Please try again. You should write ONLY name")

@input_error
def show_all(contacts):
    """show-all function show all contacts which has in the phone book"""
    if contacts:
        for name, phone in contacts.items():
            return "\n".join([f"{name}: {phone}"])
    else:
        raise ValueError ("No contacts available")

def main():
    """main function where everything happening"""
    contacts = {}
    print("\n💫 Welcome to the assistant bot!🌟")

    while True:
        """this cycle will work until user not write command "close or exit"""
        print("""
        WRITE COMMAND:
            For example:
                - hello
                - add username phone
                - change username phone
                - phone username
                - all
                - close or exit""")
        user_input = input("\nEnter a command:")
        command, *args = parse_input(user_input)
        
        if command in ["close", "exit"]:
            """these commands are letters' independed and for 
        each command call function which is written in the top"""
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command")

if __name__ == "__main__":
    main()
from book import AddressBook, Record

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me correct input data."
        except IndexError:
            return "Enter user name"
        except KeyError:
            return "Contact not found."
        except AttributeError:
            return "Invalid value"

    return inner


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    name, phone = args
    try:
        record = contacts.find(name)
        return f"Contact {record.name.value} already exists"
    except:
        record = Record(name)
        record.add_phone(phone)
        contacts.add_record(record)
        return "Contact added."


@input_error
def add_birthday(args, contacts):
    name, birthday = args
    record = contacts.find(name)
    record.add_birthday(birthday)
    return f"Contact {record.name.value} updated"
   
    

@input_error
def change_contact(args, contacts):
    name, phone = args
    record = contacts.find(name)
    record.edit_phone(phone)
    return "Contact updated."


def show_phone(args, contacts):
    name = args[0]
    record = contacts.find(name)
    return record.show_phone()
    

def show_birthday(args, contacts):
    name = args[0]
    record = contacts.find(name)
    return record.show_birthday()
    

def show_all(contacts):
    try:
        return contacts.__str__()
    except:
        return "Adressbook is empty"
    
def birthdays(contacts):
    try:
        str_b=''
        birthdays_dict = contacts.show_birthdays()
        for day,name in birthdays_dict.items():
            phones = contacts.find_phone(name)
            str_b += f'{day}: {name} {phones}\n'
        if str_b != '':
            return str_b.strip()
        else:
            return "No birthdays"
    except:
        return "Adressbook is empty"


def main():
    contacts = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
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
        elif command == "add-birthday":
            print(add_birthday(args,contacts))
        elif command == "show-birthday":
            print(show_birthday(args,contacts))
        elif command == "birthdays":
            print(birthdays(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()

from collections import UserDict
from datetime  import datetime
from get_birthday import get_birthdays_per_week


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self,name):
        super().__init__(name)

class Phone(Field):
    def __init__(self, phone):
        if len(phone) == 10:
            super().__init__(phone)
        else:
            print('Invalid phone number')
            raise ValueError('Invalid phone number')

class Birthday(Field):
    def __init__(self,value):
        try:
            birthday = datetime.strptime(value, '%d.%m.%Y')
            super().__init__(birthday.strftime('%d.%m.%Y'))
        except:
            print("Invalid format of the birthday")
            raise ValueError("Invalid format of the birthday")


class Record:
    def __init__(self, name,birthday = None):
        self.name = Name(name)
        self.phones = []
        self.birthday = Birthday(birthday) if birthday else None
        
    def add_birthday(self,birthday):
        self.birthday = Birthday(birthday)

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        for i in self.phones:
            if i.value == phone:
                self.phones.remove(Phone(i))

    def edit_phone(self, phone, new_phone):
        for i in self.phones:
            if i.value == phone:
                i.value = new_phone
                return

    def find_phone(self, phone):
        for i in self.phones:
            if i.value == phone:
                return i.value
    
    def show_phone(self):
        return f"phones: {'; '.join(p.value for p in self.phones)}"
        
    
    def show_birthday(self):
        return (self.birthday.value.strftime('%d.%m.%Y'))

            
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):

    def __init__(self):
        super().__init__()
        self.data = {}

    def add_record(self, record):
        name = record.name.value
        self.data.update({ name : record })

    def find(self, name):
        if self.data.get(name) != None:
            return self.data.get(name)
        else:
            raise KeyError(f"Contact {name} not found.")
    
    def find_phone(self, name):
        try:
            for key,record in self.data.items():
                if key == name:
                    return f"phones: {'; '.join(p.value for p in record.phones)}"

        except KeyError:
            return print(f"Contact {name} not found.")
    
    def delete(self, name):
        for item in self.data.items():
            if item[0] == name:
                self.data.popitem()
                return
            else:
                return print(f"Contact {name} not found.")
            
    def show_birthdays(self):
        birthdays_list = []
        for name,record in self.data.items():
            if record.birthday != None:
                birthdays_list.append({'name':name,'birthday':record.birthday.value})
        return get_birthdays_per_week(birthdays_list)
        
                                  

    def __str__(self):
        str_c =''
        for name,record in self.data.items(): 
            str_c += f"Contact name: {name}, phones: {'; '.join(p.value for p in record.phones)}, birthday: {record.birthday}\n"
        return str_c.strip()
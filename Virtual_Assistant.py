from collections import UserDict


class Field: # Base class for record fields
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field): # for storing the name of a contact
    def __init__(self, name):
        super().__init__(name)
    

class Phone(Field): # for storing a phone number
    def __init__(self, phone):
        if self.validation(phone):
            self.phone = phone
    
    def validation(self, phone):
        return phone.isdigit() and len(phone) == 10
    

class Record: # for storing information about a contact
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def __str__(self):
        return f"Contact name: {self.name.name}, phones: {'; '.join(p.phone for p in self.phones)}"

    def add_phone(self, phone):
        phone = Phone(phone)
        phone.validation()
        self.phones.append(phone)

    def remove_phone(self, phone):
        for p in self.phones:
            if p.phone == phone:
                self.phones.remove(p)
                break

    def edit_phone(self, old_phone, edit_phone):
        for p in self.phones:
            if p.phone == old_phone:
                p.phone = edit_phone
                p.validation()
                break

    def find_phone(self, number):
        for phone in self.phones:
            if phone.phone == number:
                return phone.phone
        return None


class AddressBook(UserDict): # for storing and managing records.
    def __init__(self, value):
        self.value = value

    def add_record(self, record):
        # create dictionary "data" (class Record, class Name, value name)
        self.data[record.name.name] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]
        else:
            print("I don't find")
    
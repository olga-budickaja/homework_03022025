# Завдання 2

# Створити клас Contact з полями surname, name, age, mob_phone, email.
# Додати методи get_contact, sent_message. Створити клас-нащадок UpdateContact
# з полями surname, name, age, mob_phone, email, job. Додати методи get_message.
# Створити екземпляри класів та дослідити стан об'єктів за допомогою атрибутів:
# __dict__, __base__, __bases__. Роздрукувати інформацію на екрані.

# Завдання 3

# Використовуючи код з завдання 2, використати функції hasattr(), getattr(),
# setattr(), delattr(). Застосувати ці функції до кожного з атрибутів класів,
# подивитися до чого це призводить.

# Завдання 4

# Використовуючи код з завдання 2, створити 2 екземпляри обох класів.
# Використати функції isinstance() – для перевірки екземплярів класу
# (за яким класом створені) та issubclass() – для перевірки
# і визначення класу-нащадка.

# Завдання 5

# Використовуючи код завдання 2 надрукуйте у терміналі інформацію,
# яка міститься у класах Contact та UpdateContact та їх екземплярах.
# Видаліть атрибут job, і знову надрукуйте стан класів та їх екземплярів.
# Порівняйте їх. Зробіть відповідні висновки.

# Завдання 6

# Використовуючи код завдання 2 надрукуйте у терміналі всі методи,
# які містяться у класі Contact та UpdateContact.

import inspect

class Contact:
    def __init__(self, name:str, surname:str, age:int, mob_phone:str, email:str, job:str):
        self.name = name
        self.surname = surname
        self.age = age
        self.mob_phone = mob_phone
        self.email = email
        self.job = job

class UpdateContact(Contact):
    def __init__(self, name, surname, age, mob_phone, email, job):
        super().__init__(name, surname, age, mob_phone, email, job)

    def get_message(self):
        return f"Updating contact: {self.name} {self.surname}"

contact = Contact("Elvis", "Presly", 24, "+38099-99-99-999", "elvis@gmail.com", "singer")

update_contact = UpdateContact("Evelin", "Lee", 24, "+38099-99-99-999", "elvelin@gmail.com", "actress")

# TASK 2
print(update_contact.get_message())
print(contact.__dict__)
print(Contact.__base__)
print(UpdateContact.__base__)
print(Contact.__bases__)
print(UpdateContact.__bases__)

# TASK 3
print(hasattr(contact, "name"))
print(hasattr(contact, "job"))
print(hasattr(update_contact, "surname"))

print(getattr(contact, "surname"))
print(getattr(contact, "mob_phone"))
print(getattr(update_contact, "age"))

print(setattr(contact, "surname", "Bubo4ka"))
print(setattr(contact, "age", 20))
print(setattr(update_contact, "job", "winks"))

print(contact.__dict__)
print(update_contact.__dict__)

print(delattr(contact, "surname"))
print(delattr(contact, "age"))
print(delattr(update_contact, "job"))

print(contact.__dict__)
print(update_contact.__dict__)

# TASK 4
contact1 = Contact("Мельник", "Веселий", 32, "+38099-99-99-999", "some@gmail.com", "мчс")

update_contact1 = UpdateContact("Шерлок", "Холмс", 29, "+38099-99-99-999", "some1@gmail.com", "детектив")

# print(isinstance(contact.age, int))

def check_attr_types(obj, type):
    attrs = obj.__dict__
    for key, value in attrs.items():
        if isinstance(value, type):
            print(f"{key}: {value} є {type.__name__}")
        else:
            print(f"{key}: {value} НЕ є {type.__name__}")

check_attr_types(contact, str)
check_attr_types(contact1, str)
check_attr_types(update_contact, str)
check_attr_types(update_contact1, str)

# print(issubclass(UpdateContact, Contact))
# print(UpdateContact.__class__)

def check_main_class(obj1, obj2):
    if issubclass(obj1, obj2):
        print(f"Клас {obj1.__name__} є нащадком класу {obj2.__name__}")
    else:
        print(f"Клас {obj1.__name__} не є нащадком клфсу {obj2.__name__}")

check_main_class(Contact, UpdateContact)
check_main_class(UpdateContact, Contact)

# TASK 5
print(Contact.__dict__)
print(UpdateContact.__dict__)
delattr(Contact, "job")
delattr(UpdateContact, "job")
print(Contact.__dict__)
print(UpdateContact.__dict__)

# TASK 6
def print_methods(obj):
    methods = []
    for key, value in obj.__dict__.items():
        if inspect.isfunction(value) or inspect.ismethod(value):
            if not key.startswith('__'):
                methods.append(key)
    if not len(methods):
        print(f"Class {obj.__name__} has not methods")
    else:
        print(f"Methods of class {obj.__name__}: {methods}")

print_methods(Contact)
print_methods(UpdateContact)

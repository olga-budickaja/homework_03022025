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

update_contact = UpdateContact("Elvis", "Presly", 24, "+38099-99-99-999", "elvis@gmail.com", "singer")

print(update_contact.get_message())
print(contact.__dict__)
print(Contact.__base__)
print(UpdateContact.__base__)
print(Contact.__bases__)
print(UpdateContact.__bases__)

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

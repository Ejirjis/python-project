import math
import random

# tex = "986-Maria (D@t@ Engineer) ,, 27y"

# print(tex)
# print(f"Name Is: {tex[4:10]}| {tex[28:31]} Years old ")

# Search

# phoe = "+22-224-3214"
# print(phoe.startswith("+22"))

# email = "Emad@gmail.com"
# print(email.endswith("coms"))
# print("@" in email)

# address = "5443 Gant crescent"
# print(address.find("323"))

# url = "http/api.compiny.com"
# print("api" in url)

# phone1 = "+213-324-342"
# phone2 = "23-4235-532"
# phone3 = "0024-532-543"

# print(phone1[phone1.find("-") + 1 :])
# print(phone2[phone2.find("-") + 1 :])
# print(phone3[phone3.find("-") + 1 :])

# Validation
# cuntry = "CA"
# print(cuntry.isalpha())

# phone = 3243435
# print(phone.is_integer())

# Math
# print(abs(2 - 10))

# x = random.randrange(1, 100)
# print(x)
# print(math.trunc(x))

# print()


# Claude code programe

# def calculate_discount(price , discount):


#     # if conditon
#     if price < 0 or discount <0 :
#         return "Invalid input"
#     elif discount > 100:
#         return"Invalid input"

#     final_price = price - ( price * discount/100)
#     return final_price

# result = calculate_discount(100, 101)
# print(result)


# def format_username (username):
#     cleaned = username.strip().lower()  # clean first
#     if len(cleaned) == 0:
#         return "Invalid User Name"
#     elif len(cleaned) > 15 :
#         return "Username too long"

#     return cleaned

# name = format_username("  Jirjis  asfdsfdsgsdf  ")
# print(name )


def validate_registoration(username, email, password):

    name_cleanend = username.strip().lower()

    if len(name_cleanend) == 0:
        return "Invalid one of the parameters ematy"
    elif len (name_cleanend) >15 :
        return "Usarname too long"
    elif "@" not in email or "." not in email:
        return "Invalid Email"
    elif len(password) < 8 or not any(char.isdigit() for char in password):
        return "Invalid password"
    else:
        return (name_cleanend, email , password)
    


def process_grades(grades):

    valid = []
    passed = 0
    for grade in grades :
        if 0 <=  grade  <= 100:
            valid.append (grade)

    # Loop 2 - count passed
    for grade in valid:
        if grade >= 50:
            passed += 1

    result = {

        "average": round(sum(valid) / len(valid) ,1),
        "highest": max(valid),
        "lowest": min(valid),
        "passed": passed
    }

    
    return result
    


#  🧩 Challenge 5 — File I/O
# You're building a simple note saver. Write two functions:

# def note_saveed(filename , note ):

#     with open (filename , "w") as f:
#         f.write(note)
#     return "Note saved"

        


# def read_note(filename):

#     try:
#         with open (filename , "r") as f :
#             contact = f.read()
#         return contact
#     except FileNotFoundError:
#         return "File not found"
    
# print(note_saveed("my_note.txt", "Buy groceries"))
# print(read_note("my_note.txt"))
# print(read_note("nothing.txt"))

class Contact:
    def __init__(self , name , phone , email):
        self . name = name 
        self .phone = phone 
        self . email = email 

    def show(self):
        print (f"Name {self.name} , Phone Number {self . phone }, Email is {self .email }")

class ContactBook:
    def __init__(self):
        self.contacts  = []


    def add_contact(self, name , email , phone):
        new_contact = Contact(name , email , phone)
        self.contacts.append (new_contact)
        return "Contact Added "
    
    def show_all (self):
        for contact in self.contacts:
            contact.show()


    def search (self,name ):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                contact.show()
                return
        return "contact not found "
    
    def delete (self,name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                return "Contact not found"
        

book = ContactBook()
book.add_contact("Jirjis", "12345", "jirjis@gmail")
book.add_contact("Alix", "1254365", "alix@gmail.com")
book.show_all()
book.search("Jirjis")
book.delete("Alix")
book.show_all()
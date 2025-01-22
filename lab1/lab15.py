from datetime import datetime

class Person:
    def __init__(self, name, country, date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = datetime.strptime(date_of_birth, "%Y-%m-%d")

    def calculate_age(self):
        today = datetime.today()
        age = today.year - self.date_of_birth.year
        if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            age -= 1
        return age

    def __str__(self):
        return f"Name: {self.name}, Country: {self.country}, Date of Birth: {self.date_of_birth.date()}"

name=input("Enter your name: ")
country= input("Enter your country: ")
date_of_birth= input("Enter your DOB")
person = Person(name, country, date_of_birth)
print(person)
print(f"Age: {person.calculate_age()} years")

'''
This file contains the class that implements a person

It will use getter methods for the attributes

Retrieves first name, last name, full name, and age

'''

class Person:
    def __init__(self, name, familyName, age):
        self.name = name
        self.famN = familyName
        self.age = age

    def getName(self):
        return self.name

    def getFullName(self):
        return self.name + " " + self.famN

    def getFamilyName(self):
        return self.famN

    def getAge(self):
        return self.age

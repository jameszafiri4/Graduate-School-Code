# class person

class person:
    def __init__(self, name, familyName, age):
        self.name = name
        self.famN = familyName
        self.age  = age
    def getName(self):
        return self.name
    def getFullName(self):
        return self.name+" "+self.famN
    def getFamilyName(self):
        return self.famN
    def getAge(self):
        return self.age

def readPeople(fileName):
    infile = open(fileName, "r")
    people = {}
    for line in infile:
        info = line.split(",")
        people.update({info[0]:person(info[1], info[2], int(info[3]))})
    return people

def printPeople(people):
    print("==========================")
    print(" Nickname  Name           ")
    print("==========================")
    for k in people.keys():
        print("{0:>9}  {1:<15}".format(k,people[k].getFullName()))

def main():
    fileName = input("Enter the file name with people info: ")
    everyone = readPeople(fileName)
    printPeople(everyone)

main()



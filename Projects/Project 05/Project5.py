# this program uses a Student class as well as two child Engineer and Doctor classes
# there will be display methods within the classes; the program will test that they work by creating objects for engineer and doctor

# this is a class representing a student
class Student:
    # takes in name and age as parameters for the constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # creates a method to diplay the student with any given parameters
    def display(self):
        print("The name of the student is:", self.name)
        print("The age of the student is:", self.age)

# creating a child class inheriting from the Student class; represents Engineering Student
class Engineer(Student):
    # takes in course in addition to name and age as parameters
    def __init__(self, name, age, course):
        # calls constructor method from parent class
        Student.__init__(self, name, age)
        # creates new object for course
        self.course = course
    # creates a method to display the engineering student with given parameters
    def displayEngineer(self):
        print("The name of the engineering student is:", self.name)
        print("The age of the engineering student is:", self.age)
        print("The course that the engineering student is taking is called:", self.course)

# creating a child class inheriting from the Student class; represents Doctor
class Doctor(Student):
    # takes in hospital in addition to name and age as paramaters
    def __init__(self, name, age, hospital):
        # calls constructor method from parent class
        Student.__init__(self, name, age)
        # creates new object for hospital
        self.hospital = hospital
    # creates a method to display the doctor with given parameters
    def displayDoctor(self):
        print("The name of the doctor is:", self.name)
        print("The age of the doctor is:", self.age)
        print("The hospital that the doctor works at is called:", self.hospital)

# main function to create child class objects via instantiation and test the methods
def main():
    # creates object for engineering student
    E = Engineer("Luffy", 18, "Computer Science")
    # calls display method from Engineer class
    E.displayEngineer()
    # line to separate engineering student and doctor
    print(" ")
    # creates object for doctor
    D = Doctor("Zoro", 25, "Mass General")
    # calls display method from Doctor class
    D.displayDoctor()

# calls main function
if __name__ == "__main__":
    main()

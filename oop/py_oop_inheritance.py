class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
        
    def printname(self):
        print(self.firstname, self.lastname)
    

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationYear = year
        
    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationYear)

person_1 = Person("John", "Doe")
person_1.printname()

print("=========================")

student_1 = Student("Mike", "Olsen", 2035)
student_1.printname()
student_1.welcome()

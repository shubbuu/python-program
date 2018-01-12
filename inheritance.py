class Person():
    def __init__(self, name):
        self.name = name

    def getDetails(self):
        print('Name - ' + self.name)

class Student(Person):
    def __init__(self, name, branch):
        self.name = name
        self.branch = branch

    def getDetails(self):
        print('Name - ' + self.name)
        print('Branch - ' + self.branch)

class Teacher(Person):
    def __init__(self, name, sub):
        self.name = name
        self.sub = sub

    def getDetails(self):
        print('Name - ' + self.name)
        print('Prof. of %s' %(self.sub))

person1 = Person('MK')
student1 = Student('shubham', 'IT')
teacher1 = Teacher('RBR', 'DSA')

person1.getDetails()
student1.getDetails()
teacher1.getDetails()

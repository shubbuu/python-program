class myClass:
    def __init__(self, name, branch, year):
        self.name = name
        self.branch = branch
        self.year = year

    def printDetails(self):
        print('Name - '+ self.name)
        print('Branch - '+ self.branch)
        print('Year - '+ self.year)

student = myClass('shubham', 'IT', '3rd')
student.printDetails()

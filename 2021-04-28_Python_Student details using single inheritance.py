#Student details using single inheritance in Python
"Computer Programming Tutor,April30, 2021"

class StudentDetails:

    def __init__(self):
        self.name=input("Enter Your Name:")
        self.schname =input("Enter Your School Name:")
        self.dept = input("Enter your Department:")
        self.roll = int(input("Enter Your Roll Number:"))


class Test(StudentDetails):
    def display(self):
        print("\n=============STUDENT INFORMATION :=========")
        print("\nStudent Full Name is: ",self.name)
        print("University Name is:",self.schname)
        print("Academic Department is:", self.dept)
        print("Roll Number is:",self.roll)

obj = Test()
obj.display()
        

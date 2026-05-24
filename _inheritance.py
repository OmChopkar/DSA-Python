#---------------Single Level Inheritance---------------
# class College:
#     def college_name(self):
#         print("College: RBU")

# #syntax: class child(parent)
# class Student(College):
#     def student_info(self):
#         print("Name: Om")
#         print("Branch: MCA")

# obj=Student()
# obj.college_name()
# obj.student_info()

#---------------Multi-Level Inheritance---------------
# class College:
#     def college_name(self):
#         print("College: RBU")

# #syntax: class child(parent)
# class Student(College):
#     def student_info(self):
#         print("Name: Om")
#         print("Branch: MCA")

# class Exam(Student):
#     def subject(self):
#         print("Subject 1: C \nSubject 2: C++ \nSubject 3: Python")

# obj=Exam()
# obj.college_name()
# obj.student_info()
# obj.subject()

#---------------Multiple Inheritance---------------
# class  SubMarks:
#     math=int(input("Enter Maths Marks:"))
#     eng=int(input("Enter English Marks:"))
#     C=int(input("Enter C Marks:"))
#     python=int(input("Enter Python Marks:"))

# class PracMarks:
#     cprac=int(input("Enter C Practical Marks:"))

# class Result(SubMarks,PracMarks):
#     def total(self):
#         if self.math>=40 and self.eng>=40 and self.C>=40 and self.python>=40 and self.cprac>=40:
#             print("Pass")
#         else:
#             print("Fail")

# obj=Result()
# obj.total()

class A:
    def add(self):
        print(2+3)
class B:
    def add(self):
        print(3+6)
class C(A,B):
    def display(self):
        print("SUM")
obj=C()
obj.display()
obj.add() #calls the first method found
obj.add()
'''
Polymorphism

Compile Time (Overloading) - Python does not support method and constructor overloading; only operator
Runtime (Overriding) - Python support method and constructor overriding
'''
#  METHOD OVERRIDING
# class RBI:
#     def home_loan(self):
#         print("RBI Home Loan ROI : 8%")
    
#     def edu_loan(self):
#         print("RBI Education Loan ROI : 9%")

# class SBI(RBI):
#     def edu_loan(self): #Overriding the edu_loan method t make changes
#         print("SBI Education Loan ROI : 10%")
#         super().edu_loan() #Used to access parent class method

# obj=SBI()
# obj.edu_loan()

#CONSTRUCTOR OVERRIDING
# class RBI:
#     def __init__(self):
#         print("Parent Class Constructor")
    
# class SBI(RBI):
#     def __init__(self):
#         print("Child Class Constructor")
#         super().__init__() #Calling parent class constructor
# obj=SBI()
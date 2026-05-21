'''
Instance Variable - Only accessible via self
Depends on state of object -> if new object -> new address
'''
#Instance Variable
# class New:  
#     def __init__(self):
#         self.a=10 
# Obj1=New()
# Obj2=New()
# Obj3=New()
# #Obj1.a=20
# print(Obj1.a)
# print(Obj2.a)
# print(Obj3.a)

'''
Static values can be changed with Class name 
'''
#Static Variable
# class New:  
#     a=10
#     def __init__(self):
#         self.name="Om" 
# Obj1=New()
# Obj2=New()
# Obj3=New()
# New.a=50 #Static variable -> Value changes using Class Name -> Changes all values of a in all objects.
# print(Obj1.a)
# print(Obj2.a)
# print(Obj3.a)

# #Combination
# class College:
#     collegeName="RCOEM"
#     def __init__(self):
#         self.studentName="Om"
# principal=College()
# teacher=College()
# accountant=College()

# print(principal.collegeName,principal.studentName)
# print(teacher.collegeName,teacher.studentName)
# print(accountant.collegeName,accountant.studentName)

# College.collegeName="RBU"
# print(principal.collegeName,principal.studentName)
# print(teacher.collegeName,teacher.studentName)
# print(accountant.collegeName,accountant.studentName)

#-------------------------OOPs----------------------------
#Static Method
class Student:
    @staticmethod
    def get_personal_details(firstname,lastname):
        print("Your Personal Details:",firstname,lastname)
    
    @staticmethod
    def contact_details(mobile_no,roll_no):
        print("Your Contact Detail:",mobile_no,roll_no)
    
Student.get_personal_details("Om","Chopkar")
Student.contact_details(8767889876,101)
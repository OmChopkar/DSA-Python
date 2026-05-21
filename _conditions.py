# #Simple if
# n=int(input("Enter number: "))
# if(n>0):
#     print("Positive")
# if(n==0):
#     print("Zero")
# if(n<0):
#     print("Negative")

# #if else
# day=input("Enter any day: ")
# if day=="SATURDAY" or day=="saturday" or day=="SUNDAY" or day=="sunday":
#     print("WEEKENED")
# else:
#     print("WORKING")

# #if elif else
# marks=int(input("Enter Marks: "))
# if marks>=65:
#     print("A")
# elif marks<=65 and marks>=50:
#     print("B")
# elif marks<=50 and marks >=35:
#     print("C")
# else:
#     print("FAIL")

# #character upper/lower/digit or spl
# a=input("Enter Character: ")
# if a.isupper():
#     print("UPPER")
# elif a.islower():
#     print("Lower")
# elif a.isdigit():
#     print("Digit")
# else:
#     print("Spl Char")

# chr = ord(input("Enter any single character: ")) 
# #ord is used to convert into ASCII code
# if chr>=65 and chr<=90:
#     print("Uppercase")
# elif chr>=97 and chr<=122:
#     print("Lowercase")
# elif chr>=48 and chr<=57:
#     print("Digit")
# else:
#     print("Special Character")


# #WAP to accept three paper marks and calculate total , percentage 
# #and check if he/she is passed in all the subjects
# #so print pass else print fail if % is > 65 so and gender = "male" so he is eligible for placement else not eligible

# m1=int(input("Enter Marks of Subject1: "))
# m2=int(input("Enter Marks of Subject2: "))
# m3=int(input("Enter Marks of Subject3: "))
# total=m1+m2+m3
# print("Total Marks Obtained:",total)
# perc=(total/300)*100 #perc=total/3.0
# print("Percentage:",perc)

# if(m1>=35 and m2>=35 and m3>=35):
#     print("Student is Passed in all Subjects")
#     gender=input("Enter Gender M/F:")
#     if(perc>=65 and gender=="M"):
#         print("Eligible for Placements")
#     else:
#         print("Not Eligible for Placements")
# else:
#     print("Student is Failed in one or more Subject(s)")


# #Rating and Increment
# salary=float(input("Enter Salary: "))
# rating=float(input("Enter your performance appraisal rating: "))
# inc=0
# if rating>=1 and rating<=3:
#     inc=salary*0.1
# elif rating>=3.1 and rating<=4:
#     inc=salary*0.3
# elif rating>=4.1 and rating<=5:
#     inc=salary*0.4
# else:
#     print("Invalid Ratings")
# print("Incremented Salary: ",inc+salary)

# #Salary, TA, DA, HRA and Gross Salary
# basicSalary=int(input("Enter Salary: "))
# HRA=basicSalary*0.2
# TA=basicSalary*0.3
# DA=basicSalary*0.45
# print("HRA:",HRA)
# print("TA:",TA)
# print("DA:",DA)
# print("Gross Salary: ",basicSalary+HRA+TA+DA)
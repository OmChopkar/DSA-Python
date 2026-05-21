'''
Why to use file handling?
'''
# import csv
# f=open("emp.csv",'a')
# a = csv.writer(f)
# # a.writerow(["Emp_ID","Emp_Name","Emp_Age"])
# id=int(input("Enter Employee ID:"))
# name=input("Enter Employee Name:")
# age=int(input("Enter Employee Age:"))
# a.writerow([id,name,age])

import csv
f=open("student.csv",'a',newline="")
a = csv.writer(f)
# a.writerow(["Student_ID","Student_Name","Physics","Chemistry","Maths","Total","Percentage","Result"])
id=int(input("Enter Student ID:"))
name=input("Enter Student Name:")
phy=int(input("Enter Physics Marks:"))
chem=int(input("Enter Chemistry Marks:"))
math=int(input("Enter Maths Marks:"))
total=phy+chem+math
perc=(total/300)*100
if phy>=40 and math>=40 and chem>=40:
    res="Pass"
else:
    res="Fail"
a.writerow([id,name,phy,chem,math,total,perc,res])
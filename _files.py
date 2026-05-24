'''
Why to use file handling?
'''
# import csv
# f=open("emp.csv",'a')
# a = csv.writer(f)
# # a.writerow(["Emp_ID","Emp_Name","Emp_Age"]) #Comment the line after executing it one time
# id=int(input("Enter Employee ID:"))
# name=input("Enter Employee Name:")
# age=int(input("Enter Employee Age:"))
# a.writerow([id,name,age])

# import csv
# f=open("student.csv",'a',newline="")
# a = csv.writer(f)
# # a.writerow(["Student_ID","Student_Name","Physics","Chemistry","Maths","Total","Percentage","Result"]) #Comment the line after executing it one time
# id=int(input("Enter Student ID:"))
# name=input("Enter Student Name:")
# phy=int(input("Enter Physics Marks:"))
# chem=int(input("Enter Chemistry Marks:"))
# math=int(input("Enter Maths Marks:"))
# total=phy+chem+math
# perc=(total/300)*100
# if phy>=40 and math>=40 and chem>=40:
#     res="Pass"
# else:
#     res="Fail"
# a.writerow([id,name,phy,chem,math,total,perc,res])

#Program to print the number of lines, words and characters preent in the given file.
import os
import sys 

fname=input("Enter file name:")
if os.path.isfile(fname):
    print("File exists:",fname)
    f=open(fname,"r")
else:
    print("File does not exist:",fname)
    sys.exit(0)
lcount=wcount=ccount=0
for line in f:
    lcount+=1
    ccount=ccount+len(line)
    words=line.split()
    wcount+=len(words)
print("The number of Lines:",lcount)
print("The number of Words:",wcount)
print("The number of Characters:",ccount)
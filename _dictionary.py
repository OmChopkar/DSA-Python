# mydict={
#     101:"Om",
#     102:"Ashish",
#     "103":"Mohini",
#     "104":"Trivani",
#      101: "Ashish", #101 updated to Ashish
#      104:"Ashish"
# }
# print(mydict)

# #print(dict_name[key])
# print(mydict[101])

# # Changing Value
# # dict_name[key]=newvalue
# mydict[101]="Om"
# print(mydict)

# #Accesing Keys
# for i in mydict:
#     print(i)

# #Accessing Values
# for i in mydict.values():
#     print(i)

# #Key Value Pair
# for i,j in mydict.items():
#     print(i, j)

# #New key value pair
# #dict_name[key]=value
# mydict["Mobile"]=8372882716
# mydict["Dept"]="Management"
# print(mydict)

# #Remove pair 
# #dict_name.pop(key)
# mydict.pop(101)
# print(mydict)

# a={(1,2):1,(2,3):2,(4,5):3} #tuple as a key
# print(a[4,5])

# a={'a':1,'b':2,'c':3}
# print(a['a','b']) #Error : Two keys cannot be accessible at the same time

#-----------------------------------------------------------------------------
# arr = {}
# arr[1]=1
# arr['1']=2
# arr[1]+=1 #Value is appended by 1
# print(arr)
# sum=0
# for k in arr:
#     sum+=arr[k]
# print(sum)

#-----------------------------------------------------------------------------
# arr = {}
# arr[1]=1
# arr['1']=2
# print(arr)
# arr[1.0]=4 #Value changed  
# print(arr)
# sum=0
# for k in arr:
#     sum+=arr[k]
# print(sum)

#-----------------------------------------------------------------------------
# mydict={}
# mydict[(1,2,4)]=8
# mydict[(4,2,1)]=10
# mydict[(1,2)]=12
# print(mydict)
# sum=0
# for k in mydict:
#     sum+=mydict[k]
# print(sum)
#-----------------------------------------------------------------------------

# box={}
# jars={}
# crates={}
# box['biscuits']=1
# box['cake']=3
# jars['jam']=4
# crates['Box']=box
# crates['Jars']=jars
# print(box)
# print(jars)
# print(crates)
# print(len(crates[box])) #TypeError because accessing key which value is dictionary 

#-----------------------------------------------------------------------------
# dict={'c':97,'a':96,'b':98} 
# for _ in sorted(dict): #sorting key wise
#     print(dict[_])

# rec={1:1,2:2}
# print(id(rec))
# r=rec.copy() #Copy not assigned 
# print(id(r))
# print(id(r)==id(rec)) #false because copied not assigned

# rec={"Name":"Python","Age":20}
# id1=id(rec)
# print("id1: ",id1)
# del rec
# rec={"Name":"Python","Age":20}
# id2=id(rec)
# print("id2: ",id2)
# print(id1==id2) #True because id1 is stored; and after rec again with same valies, the id is same.

# mydict={"A":50,"B":30,"C":70}
# max=0
# for i in mydict.values():
#     if i>max:
#         max=i
# print(max)

# mydict={"A":50,"B":30,"C":70}
# min=mydict["A"]
# for i in mydict.values():
#     if i<min:
#         min=i
# print(min)

#########################################################################
# l1=[1,2,2,3,4,3,5]
# #l2={1:1,2:2,3:2,4:1,5:1}
# l2 = {}
# for i in l1:
#     if i not in l2:
#         l2[i] = 1 
#     else:
#         l2[i] += 1 
# print(l2)

#-----------------------------------------------------------------------------

# fruit={}
# def addone(index):
#     if index in fruit:
#         fruit[index]+=1
#     else:
#         fruit[index]=1
# addone("1")
# addone("2")
# addone("1.0")
# print(len(fruit))

#-----------------------------------------------------------------------------
#WAP to accept student name and marks from the keyboard and created a dictionary.
#Also display marks by taking student name

# student={}
# N=int(input("Enter number of students: "))
# for i in range(N):
#     print()
#     name=input("Enter Student Name: ")
#     marks=int(input("Enter Student Marks: "))
#     student[name]=marks

# while True:
#     print()
#     name=input("Enter Student Name to get Marks: ")
#     marks=student.get(name,-1)

#     if marks==-1:
#         print("Student Not Found.")
#     else:
#         print(f"Marks of {name} is {marks}.")

#     ch=input("Do you want to continue? (Y/N): ")
#     if ch=="No":
#         break
# print("Thank You.")

#-----------------------------------------------------------------------------
# #Dictionary comprehension
# squares={x:x*x for x in range(1,6)}
# print(squares)

# doubles={x:2*x for x in range(1,6)}
# print(doubles)
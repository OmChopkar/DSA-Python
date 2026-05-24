'''
Python Collections - list, tuple, set, dictionary

List:
-Order wise data
-Heterogeneous data
-Represented []
-Duplicates values allowed
-List by nature is growable
-Mutable

list	              tuple
[]		            () optional
mutable		        immutable
req not fixed	    req fixed
'''
# myList=["Om","Ashish","Komal","Ankush",77,"Sandip",True,3.14,7]
# print(myList)
# print(type(myList))
# print(myList[0])
# print(myList[-1])
# print(myList[2:5])
# print(myList[:5])
# print(myList[0:9:2])

#Changing value
# myList[2]="Akshay"
# print(myList)

# #Checking if Value in List
# if "Ankush" in myList:
#     print("YES")
# else:
#     print("NO")

# #Appending value on top ie right side
# myList.append("Harsh") 
# myList.append("Laxman")
# print(myList)

# #insert to add item in specific location
# myList.insert(3,"Sanket") 
# print(myList)

# myList.remove(True)
# print(myList)

# newList=myList.copy() #cloning
# print(newList)

# if myList == newList:
#     print("YES.")

# myList=[["Om","Chopkar"],[82.4],[440033,"Nagpur"]]
# print(myList)
# #print(myList[row][col])
# print(myList[0][0])
# print(myList[0][1])
# print(myList[1][0])
# print(myList[2][0])
# print(myList[2][1])

# list2=[50,25.23,"Om"]
# del list2[2] #deleted specific index value
# del list2 #deletes the list completely
# # list2.clear() #Clears the list
# print(list2)

# name="OmDhanraj"
# print(name)
# myName=list(name) #typecasting
# print(myName)

# myList=[83,21,9,65,15]
# print(myList)
# myList.sort()
# print(myList)

# myList=[83,21,9,65,15]
# myList.sort(reverse=True)
# print(myList)

# myList=[83,21,9,65,15]
# newList=myList
# print(id(myList))
# print(id(newList))

# myList[0]=99
# print(newList)

# myList=[83,21,9,65,15]
# for i in myList:
#     print(i)

# #Push 0 at the end
# ip=[0,1,4,0,2,5]
# # op=[1,4,2,5,0,0]
# for i in ip:
#     if i==0:
#         ip.remove(i)
#         ip.append(i)
# print(ip)

# a=[7,3,2,8,9]
# a.sort()
# print(a)
# print(a[-2])

# a=[1,2,3,4,5,6,7,8,9]
# a[::2]=[10,20,30,40,50,50] #ValueError: attempt to assign sequence of size 6 to extended slice of size 5
# print(a)

# a=[1,2,3,4,5]
# print(a[3:0:-1]) #3 starting; stop 1; dec by -1

# a=[[1,2,3,4],[4,5,6,7],[8,9,10,11],[12,13,14,15]]
# for i in range(0,4): #Only focused on outer loop; no inner loop
#     print(a[i].pop())

# fruit_list1=['Apple','Banana','Cherry','Papaya']
# fruit_list2=fruit_list1
# fruit_list3=fruit_list1[:]
# fruit_list2[0]='Guava'
# fruit_list3[1]='Kiwi'
# sum=0
# for ls in (fruit_list1,fruit_list2,fruit_list3):
#     if ls[0]=='Guava':
#         sum+=1
#     if ls[1]=='Kiwi':
#         sum+=20
# print(sum)

# A=[1,2,3]
# B=[2,3,4]
# C=[3,4,5]
# for i in A:
#     if i in B and i in C:
#         print(i)

# #Diff of adjacents, then sum
# N = int(input("Enter Size:"))
# mylist=[]
# for i in range(N):
#     val=int(input("Enter Values: "))
#     mylist.append(val)
# print(mylist)
# sum=0
# # print(len(mylist))
# for i in range (len(mylist)-1):
#     if i+1 in range(len(mylist)):
#         sum+=abs(mylist[i]-mylist[i+1])
# print(sum)



#-------------------------------------------------------------------
# Input: [1,0,1,1,1,0,1,1,1,1]
# Output: 4
# ip = [1, 0, 1, 1, 1, 0, 1, 1, 1, 1]
# max = 0 
# count = 0 
# for num in ip:
#     if num == 1:
#         count += 1
#         if count > max:
#             max = count
#     else:
#         count = 0
# print(max) 

#-----------------------------------
#INPUT = 578378923
#OUTPUT = 3 => 7,8,3 are repeating

# mylist=[5,7,8,3,7,8,9,2,3]
# newlist=[]
# for i in range(len(mylist)):
#     key=mylist[i]
#     j=i+1
#     while j<len(mylist):
#         if key==mylist[j]:
#             newlist.append(key)
#         j+=1
# print(len(newlist))

#---------------------------------------
# v=['a','e','i','o','u']
# w=input("Enter Word: ")
# found=[]
# for i in w:
#     if i in v:
#         if i not in found:
#             found.append(i)
# print("Vowels Found:",found)
# print("unique vowels",len(found),"from the given word",w)

# num, start, end = map(int, input().split())
# List=[]
# for i in range(num):
#     a=int(input())
#     List.append(a)

# for j in List:
#     if j>=start and j<=end:
#         print(j,end=' ')

# import datetime
# date=datetime.datetime.now()
# print("Its now:{:%Y-%m-%d %H:%M:%S}".format(date))

# x=['A','B','C']
# y=['A','B','C']
# z=[1,2,3,4]
# print(x==y)
# print(x==z)
# print(x!=z)

#s=[1,4,9,16,25,36,49,64,81,100]
# s=[i*i for i in range(1,11)]
# print(s)

# val=[2**i for i in range(1,6)]
# print(val)


# #List Comprehension
# a,b=[int(x) for x in input("Enter Two Numbers: ").split()]
# print("Product: ",a*b)

# a,b,c=[float(x) for x in input("Enter Three Numbers: ").split()]
# print("Sum: ",a+b+c)
'''
Find first non repeating character
INPUT="leetcode"
OUTPUT="l"
'''
# string=input()
# L=[]
# for i in string:
#     if i not in L:
#         L.append(i) 
#     else:
#         L.remove(i)
# print(L[0])

#----------------------------------------
#INPUT=[1,2,3,4,5]
#OUTPUT=[4,5,1,2,3]
# INPUT=[1,2,3,4,5]
# OP=[]
# for i in range(len(INPUT)):
#     OP=INPUT[3:]+INPUT[0:3]
# print(OP)

#-------------------------------------------
# def isPalindrome(self, x):
#     og=x
#     rev=0
#     while(x>0):
#         digit=x%10
#         rev=(rev*10)+digit
#         x=x//10
#     if rev==og:
#         return True
#     else:
#         return False

#-------------------------------------------
# Reverse each word in a Strings
# Hello World
# olleH dlroW

# str1, str2=map(str, input().split())
# rev1=""
# rev2=""
# for i in range(len(str1)-1,-1,-1):
#     rev1+=str1[i]
# for i in range(len(str2)-1,-1,-1):
#     rev2+=str2[i]
# print(rev1,rev2)

#-------------------------------------------
# Check for Valid Parenthesis
# INPUT: "({[]})"
# OUTPUT: VALID
# brackets=input("")
# stack=[]
# for i in brackets:
#     if i in "({[":
#         stack.append(i)

#-------------------------------------------
# #INPUT= [4,3,2,7,8,2,1,5,5]
# #OUTPUT=[2,5]
# nums=list(map(int, input().split()))
# dict={}
# for i in nums: 
#     if i in dict:
#         dict[i]+=1
#     else:
#         dict[i]=1
# result=[]
# for key in dict:
#     if dict[key]>1:
#         result.append(key)
# print(result)

#-------------------------------------------

# #INPUT= {"C":3,"B":2,"A":1}
# #Ascending by key= {"A":1, "B":2,"C":3}
# #Descending by value= {"C":3,"B":2,"A":1}

# INPUT={"C":3,"B":2,"A":1}
# #Key Ascending  

#-------------------------------------------
#INPUT=[0,0,1,2,0,3,0,0,4]
#OUTPUT=[1,2,0,3,0,0,4]
# INPUT=[0,0,1,2,0,3,0,0,4]
# i=0
# while INPUT[i]==0:
#     i+=1
# print(INPUT[i:])

#-------------------------------------------
# #INPUT=[3,4,-1,1]
# #OUTPUT=2
# ip=[3,4,-1,1]
# for i in range(1,len(ip)):
#     if i>0 and i not in ip:
#         print (i)
#         break
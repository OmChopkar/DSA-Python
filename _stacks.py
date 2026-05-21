''''
STACK: LIFO
IRL: Search history always last searcj on top
STACK IMPLEMENTATION
1. List/Array
2. Linked List

Queue/Stack using List
-Easy to implement
-Speed problem when it grows

Queue/Stack using Linked List
-Fast Performance 
-Implementation not east

                        Time                        Space
Create Stack            O(1)                        O(1)
Push                    O(1)/O(n^2)                 O(1)
Pop                     O(1)                        O(1)
Peek                    O(1)                        O(1)
isEmpty                 O(1)                        O(1)
Delete Entire Stack     O(1)                        O(1)
'''
# #Stack Implementation using List/Array -> No Size Limit
# class Stack:
#     def __init__(self):
#         self.myStack=[] #Empty Stack 

#     def push(self, value):
#         self.myStack.append(value)
#         print("Element Pushed.")
    
#     def display(self):
#         print(self.myStack)
    
#     def isEmpty(self):
#         if self.myStack==[]:
#             return True
#         else:
#             return False
    
#     def pop(self):
#         if self.isEmpty():
#             print("Stack is Empty")
#         else:
#             print(self.myStack.pop())
    
#     def peek(self):
#         if self.isEmpty():
#             print("Stack Empty")
#         else:
#             print(self.myStack[-1])
    
#     def deleteStack(self):
#         self.myStack=None

# obj=Stack()
# print("Stack Created.")
# while True:
#     print()
#     print("--STACK MENU OPERATIONS--")
#     print("1. Push Operation")
#     print("2. Display")
#     print("3. Pop Operation")
#     print("4. Peek Operation")
#     print("5. Delete Stack")
#     print("7. Exit")
#     ch=int(input("Enter Your Choice:"))
#     if ch==1:
#         value=int(input("Enter value to push: "))
#         obj.push(value)
#     elif ch==2:
#         obj.display()
#     elif ch==3:
#         obj.pop()
#     elif ch==4:
#         obj.peek()
#     elif ch==5:
#         obj.deleteStack()
#     else:
#         exit()

# ----------------------------------------------------------------

# #Stack Implementation using List/Array -> Size Limit
# class Stack:
#     def __init__(self, size):
#         self.myStack=[] #Empty Stack 
#         self.stackSize=size #size defined 

#     def push(self, value):
#         if self.isFull():
#             print("Stack is Full.")
#         else:
#             self.myStack.append(value)
#             print("Element Pushed.")
       
#     def display(self):
#         print(self.myStack)
    
#     def isEmpty(self):
#         if self.myStack==[]:
#             return True
#         else:
#             return False
    
#     def isFull(self):
#         if len(self.myStack)==self.stackSize:
#             return True
#         else:
#             return False
    
#     def pop(self):
#         if self.isEmpty():
#             print("Stack is Empty")
#         else:
#             print(self.myStack.pop())
    
#     def peek(self):
#         if self.isEmpty():
#             print("Stack Empty")
#         else:
#             print(self.myStack[-1])
    
#     def deleteStack(self):
#         self.myStack=None

# size=int(input("Enter Size of Stack: "))
# obj=Stack(size)
# print("Stack Created.")
# while True:
#     print()
#     print("--STACK MENU OPERATIONS--")
#     print("1. Push Operation")
#     print("2. Display")
#     print("3. Pop Operation")
#     print("4. Peek Operation")
#     print("5. Delete Stack")
#     print("7. Exit")
#     ch=int(input("Enter Your Choice:"))
#     if ch==1:
#         value=int(input("Enter value to push: "))
#         obj.push(value)
#     elif ch==2:
#         obj.display()
#     elif ch==3:
#         obj.pop()
#     elif ch==4:
#         obj.peek()
#     elif ch==5:
#         obj.deleteStack()
#     else:
#         exit()

# ----------------------------------------------------------------
# INPUT: 572378233 3
# #OUTPUT: 3
# mylist=[5,7,8,3,7,8,9,2,3]
# newlist={}
# for i in range(len(mylist)):
#     count=0
#     key=mylist[i]
#     j=1
#     while j<len(mylist):
#         if key==mylist[j]:
#             count+=1
#         j+=1
#     if count>1:
#         newlist[key]=count
# max=newlist
# print(max)

#----------------------------------------------------------------
# STUDENT MANAGEMENT SYSTEM
# 1. Add -> Student ID, Roll No, Name, City
# 2. Show -> ID RollNo Name City
# 3. Update -> Ask ID : Displays details in numbers 1,2,3,4 Do not update 
#      Choice 1,2,3 -> Each detail update
# 4. Delete
# 5. Exit


# #----------------------------------------------------------------
# N=int(input())
# num=list(map(int,input().split()))
# count=0
# for i in 
#     if int(num**0.5)**2==num:
#         count+=1
# print(count)

#-------------------IMPLEMENTATION USING LINKED LIST------------------
class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    
    def __iter__(self): #python generator function;  Iteration faster for large dataset
        curNode=self.head
        while curNode:
            yield curNode #yield is used to return 
            curNode = curNode.next

class Stack:
    def __init__(self):
        self.LinkedList=LinkedList()
    
    def __str__(self):
        values=[str(x.value) for x  in self.LinkedList]
        return '\n'.join(values)

    def isEmpty(self):
        if self.LinkedList.head is None:
            return True
        else:
            return False
    
    def push(self,value):
        node=Node(value)
        node.next=self.LinkedList.head
        self.LinkedList.head=node 
    
    def pop(self):
        if self.isEmpty():
            return "There is no element in stack"
        else:
            nodeValue=self.LinkedList.head.value #Optional
            self.LinkedList.head=self.LinkedList.head.next
            return nodeValue #Optional -> returning the value which is popped
        
    def peek(self):
        if self.isEmpty():
            return "There is no element in stack"
        else:
            nodeValue=self.LinkedList.head.value
            return nodeValue
            
    def delete(self):
        self.LinkedList.head=None

customStack=Stack()
customStack.push(1)
customStack.push(2)
customStack.push(3)
print(customStack)
print("\nTop Element:",customStack.peek())
print("\nPop Top ELement:",customStack.pop())
print("\nStack after pop operation:")
print(customStack)
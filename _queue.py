'''
DATE - 16.05.2026
QUEUE DS
1. Enque
2. Deque
3. Display
4. isEmpty()
5. isFull()
6. Delete
7. peek()

                        Time                        Space
Create Queue            O(1)                        O(1)
Enqueue                 O(n)                        O(1)
Dequeue                 O(n)                        O(1)
Peek                    O(1)                        O(1)
isEmpty                 O(1)                        O(1)
Delete Entire Queue     O(1)                        O(1)
'''
# #Queue Implementation using List/Array -> Size Limit
# class Queue:
#     def __init__(self, size):
#         self.myQueue=[] #Empty Stack 
#         self.queueSize=size #size defined 
    
#     def isFull(self):
#         if len(self.myQueue)==self.queueSize:
#             return True
#         else:
#             return False

#     def EnQueue(self, value):
#         if self.isFull():
#             print("Queue is Full.")
#         else:
#             self.myQueue.append(value)
#             print("Element Inserted.")
    
#     def display(self):
#         print(self.myQueue)
    
#     def isEmpty(self):
#         if self.myQueue==[]:
#             return True
#         else:
#             return False

#     def DeQueue(self):
#         if self.isEmpty()==[]:
#             print("Queue is Empty")
#         else:
#             self.myQueue.pop(0)

#     def peek(self):
#         if self.isEmpty():
#             print("Queue Empty")
#         else:
#             print(self.myQueue[0])
    
#     def deleteQueue(self):
#         self.myQueue=None

# size=int(input("Enter Size of Queue: "))
# obj=Queue(size)
# print("Queue Created.")

# while True:
#     print()
#     print("--Queue MENU OPERATIONS--")
#     print("1. Enqueue Operation")
#     print("2. Display Queue")
#     print("3. DeQueue Operation")
#     print("4. Peek Operation")
#     print("5. Delete Queue")
#     print("6. Exit")

#     ch=int(input("Enter Your Choice:"))

#     if ch==1:
#         value=int(input("Enter value to insert: "))
#         obj.EnQueue(value)

#     elif ch==2:
#         obj.display()

#     elif ch==3:
#         obj.DeQueue()

#     elif ch==4:
#         obj.peek()

#     elif ch==5:
#         obj.deleteQueue()

#     elif ch==6:
#         exit()

#----------------QUEUE USING LINKED LIST-----------------------
class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None

    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def __iter__(self):
        curNode=self.head
        while curNode:
            yield curNode
            curNode=curNode.next

class Queue:
    def __init__(self):
        values=[str(x) for x in self.LinkedList]
        return ' '.join(values)
    
    def enQueue(self,value):
        newNode = Node(value)
        if self.LinkedList.head is None:
            self.LinkedList.head=newNode
            self.LinkedList.next=newNode
        else:
            self.LinkedList.tail.next=newNode
            self.LinkedList.tail=newNode
    
    def isEmpty(self):
        if self.LinkedList.head is None:
            return True
        else:
            return False

    def deQueue(self):
        if isEmpty():
            return "Empty"
        else:
            tempNode=self.LinkedList.head
            if self.LinkedList.head==self.LinkedList.tail:
                self.LinkedList.head=None
                self.LinkedList.tail=None
            else:
                self.LinkedList.head=self.LinkedList.head.next
            return tempNode
    
    def peek(self):
        if isEmpty():
            return "Empty"
        else:
            return self.LinkedList.head

    def delete(self):
        self.LinkedList.head=None
        self.LinkedList.tail=None

customQueue=Queue()
customQueue.enQueue(1)
customQueue.enQueue(2)
customQueue.enQueue(3)
print(customQueue)
print("\nTop Element:",customQueue.peek())
print("\nPop Top ELement:",customQueue.seQueue())
print("\nStack after pop operation:")
print(customQueue)
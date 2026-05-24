# class Node:
#     def __init__(self, data):
#         self.data=data #Instance variable
#         self.next=None

# class Linkedlist:
#     def __init__(self):
#         self.head=None

# linkedlist=Linkedlist()

# linkedlist.head=Node(5)
# second=Node(10)
# third=Node(15)
# fourth=Node(20)

# #Connecting nodes
# linkedlist.head.next=second
# second.next=third
# third.next=fourth
# fourth.next=None

# #Traversing Linked List
# while linkedlist.head != None:
#     print(linkedlist.head.data,"|"," ->")
#     linkedlist.head=linkedlist.head.next

# #----------DYNAMIC LINKED LIST----------
class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def addNode(self,value):
        self.node = Node(value) #Node class object
        if self.head is None:
            self.head=self.node
            self.tail=self.node
        else:
            self.tail.next=self.node
            self.tail=self.node

    def addNodeBeginning(self,value):
        self.node=Node(value)
        if self.head is None:
            self.head=self.node
            self.tail=self.node
        else:
            self.node.next=self.head
            self.head=self.node

    def  addNodeBetween(self,index,value): 
        node = Node(value)  
        if self.head is None:  
            self.head = node  
            self.tail = node  
        elif index ==0:  
            node.next = self.head  
            self.head = node  
        else:  
            temp = self.head  
            for _ in range(index-1):  
                temp = temp.next  
            node.next = temp.next  
            temp.next = node
        
    def display(self):
        while self.head != None:
            print(self.head.data,"|",self.head.next," ->",end=' ')
            self.head=self.head.next
        
if __name__=='__main__':
    obj=LinkedList()
    while True:
        print()
        print("\n---LINKED LIST MENU---")
        print('1. Add Node LinkedList')
        print('2. Add Node in Beginning')
        print('3. Add Node in Between')
        print('4. Add Node in End')
        print('5. Display Linked List')
        print('6. Exit')
        print()
        ch=int(input('Enter your choice:'))
        if ch==1:
            value=int(input('Enter value to node:'))
            obj.addNode(value)
            print('Node added successfully')
        
        elif ch==2:
            value=int(input('Enter value to node:'))
            obj.addNodeBeginning(value)
            print('Node added successfully')

        elif ch==3:
            index=int(input('Enter index to add node:'))
            value=int(input('Enter value to node:'))
            obj.addNodeBetween(index,value)
            print('Node added successfully')
            
        elif ch==5:
            print("Linked List:")
            obj.display()
        
        elif ch==6:
            exit()
'''
---TREE DATA STRUCTURE---
Non Linear data structure
Used to represent hierarchical data
Ex- file system

Can be implemented using :
- Linked list 
- Array

[] [Root] [LeftChild] [RightChild] [Left-LeftChild] [Left-RightChild] [Right-LeftChild] [Right-RightChild]

                                Time                    Space
Creation                        O(1)                     O(1)
Insertion                       O(n)                     O(1)
Searching                       O(n)                     O(1)
Traversing                      O(n)                     O(1) 
Deletion of Node                O(n)                     O(1)
Deletion of Linked List         O(1)                     O(1)
'''
# class Tree:
#     def __init__(self,data):
#         self.data=data
#         self.child=[]

#     def __str__(self,level=0):
#         ret="   "*level+str(self.data)+"\n"
#         for child in self.child:
#             ret+=child.__str__(level+1)
#         return ret

#     def addChild(self,object):
#         self.child.append(object)
#     print("Tree Node Added")

# rootNode=Tree("N1")
# N2=Tree("N2")
# N3=Tree("N3")
# N4=Tree("N4")
# N5=Tree("N5")
# N6=Tree("N6")
# N7=Tree("N7")
# N8=Tree("N8")

# rootNode.addChild(N2)
# rootNode.addChild(N3)
# N2.addChild(N4)
# N2.addChild(N5)
# N3.addChild(N6)
# N4.addChild(N7)
# N4.addChild(N8)

# print(rootNode)


# rootNode=Tree("Drinks")
# Hot=Tree("Hot")
# Cold=Tree("Cold")
# Tea=Tree("Tea")
# Coffee=Tree("Coffee")
# NonAlcoholic=Tree("Non-Alcoholic")
# Alcoholic=Tree("Alcoholic")
# GreenTea=Tree("Green Tea")
# BlackTea=Tree("Black Tea")

# rootNode.addChild(Hot)
# rootNode.addChild(Cold)
# Hot.addChild(Tea)
# Hot.addChild(Coffee)
# Cold.addChild(NonAlcoholic)
# Cold.addChild(Alcoholic)
# Tea.addChild(GreenTea)
# Tea.addChild(BlackTea)

# print(rootNode)

#-----------------------
'''
Types of Trees:

-Binary Tree-
0,1, or max 2 child.

-Full  Binary Tree-
0 or 2 child
No node has a single child

-Complete Binary Tree-
All levels except possibly the last are completely filled
Nodes in the last level are filled from left to right

-Perfect Binary Tree-
All leaf node at same level
All internal nodes have exactly two nodes

Operations of Trees:
Creation of tree
Insertion of a node
Deletion of node
Search for a value
Traverse all nodes
Deletion of tree

Part of Depth First Search:
Preorder- ROOT LEFT RIGHT
Inorder- LEFT ROOT RIGHT
Postorder- LEFT RIGHT ROOT

Breadth First Search - Oreder Level Traversal

Why BST?
Performs faster then Binary Tree when inserting and deleting the node.

Left child value < root node
Right child value > root node

Preorder-
Inorder-10,20,30,40,50,60,70,80,90,100
Postorder-
'''
class BSTNode:
    def __init__(self, data):
        self.data=data
        self.leftChild=None
        self.rightChild=None

def insertNode(rootNode,nodeValue):
    if rootNode.data==None:
        rootNode.data=nodeValue
    elif nodeValue<=rootNode.data:
        if rootNode.leftChild is None:
            rootNode.leftChild=BSTNode(nodeValue)
        else:
            insertNode(rootNode.leftChild,nodeValue)
    else:
        if rootNode.rightChild is None:
            rootNode.rightChild=BSTNode(nodeValue)
        else:
            insertNode(rootNode.rightChild,nodeValue)

def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data,end=" ")
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data,end=" ")
    inOrderTraversal(rootNode.rightChild)

def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data,end=" ")

def searchNode(rootNode,nodeValue):
    if rootNode.data==nodeValue:
        print("Found.")
    elif nodeValue<rootNode.data:
        if rootNode.leftChild is None:
            print("Not Found")
        else:
            searchNode(rootNode.leftChild,nodeValue)
    else:
        if rootNode.rightChild is None:
            print("Not Found")
        else:
            searchNode(rootNode.rightChild,nodeValue)

newBST=BSTNode(None)
insertNode(newBST,70)
insertNode(newBST,50)
insertNode(newBST,90)
insertNode(newBST,30)
insertNode(newBST,60)
insertNode(newBST,80)
insertNode(newBST,100)
insertNode(newBST,20)
insertNode(newBST,40)
insertNode(newBST,10)

searchNode(newBST,20)
searchNode(newBST,80)
searchNode(newBST,70)
searchNode(newBST,200)

# print("Preorder Traversal:")
# preOrderTraversal(newBST)
# print()
# print("Inorder Traversal:")
# inOrderTraversal(newBST)
# print()
# print("Postorder Traversal:")
# postOrderTraversal(newBST)
'''
Hashing is a tech used to convert data into a fixed size value called a hash value or hash code.
Hash value help us to store and search data very fast
With hasing data can be found almost instantly.

"Converting a big piece of info into small address"

Time complexity: O(1) - constant time; speed search

With hashing : Search, Insert, Delete - Constant time O(1)

Hash functions converts input -> fixed index

---
Suppose table size = 10
Index = Key % 10

Collision: all map to same index.


ASCII
C
A
T

SUM = 
Table size : 10

Index = SUM%10
'''
class Hashing:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]
    
    def hash_function(self, key):
        return key % self.size

    def insert(self, key):
        index = self.hash_function(key)
        self.table[index].append(key)
    
    def display(self):
        print(self.table)
        
h = Hashing(10)
h.insert(15)
h.insert(25)
h.insert(35)
h.display()

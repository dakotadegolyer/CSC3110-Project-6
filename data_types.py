class ListNode:
    def __init__(self, val: str):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self, lst:list):
        self.head = None
        for i in lst:
            self.insert(ListNode(str(i)))
            
    def __repr__(self):
        cur: ListNode = self.head
        output = ""
        while cur:
            output += str(cur.val) + " -> "
            cur = cur.next
        output += "None"
        return output
    
    def insert(self, node: ListNode) -> None:
        if self.head == None:
            self.head = node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = node
    
    def insert(self, val: str) -> None:
        node = ListNode(val=val)
        if self.head == None:
            self.head = node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = node

"""
basically you can index it as if it were a dictionary
example:
adjacencyList = AdjacencyList()     # init
adjacencyList["A"].insert("E")      # inserts "E" into the list for A, meaning A is connected to E
print(adjacencylist)                # prints the following showing that A is connected to E
A -> E -> None
B -> None
C -> None
D -> None
E -> None

"""
class AdjacencyList:    
    def __init__(self):
        self.lst: dict(LinkedList) = {
            "A":LinkedList([]), 
            "B":LinkedList([]), 
            "C":LinkedList([]), 
            "D":LinkedList([]), 
            "E":LinkedList([])}
        
    def __getitem__(self, key):
        return self.lst[key]
    
    def __repr__(self):
        output = ""
        for key in self.lst.keys():
            output += key + " -> " + str(self.lst[key]) + "\n"
        return output

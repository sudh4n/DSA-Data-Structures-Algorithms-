Question:

"""Problem Statement:
Write a Python program to create a linked list with three nodes and print its elements.

Expected Output
If you insert the values [10, 20, 30], the output should be:

rust
Copy
Edit
10 --> 20 --> 30 --> None
Solution Approach
Define a Node class that stores data and a pointer next.
Manually create three nodes and link them together.
Traverse and print the linked list."""

Solution:

class Node:
    def __init__(self, data):
        self.data = data  # Store the data
        self.next = None  #move pointer to next node

#Creating Nodes
node1 = Node(10) 
node2 = Node(20)  
node3 = Node(30)

#link the nodes
node1.next = node2 #10 --> 20
node2.next = node3 #20 --> 30

#print linked list
def print_linked_list(head):
  itr = head
  while itr:
    print(itr.data, "-->", end = " ")
    itr.next = itr  #move to next node
    print("None")  #Indicate end of list

print_linked_list(node1)

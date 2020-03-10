from linked_list import LinkedList
""" Showcase of how my implementation of Linked lists works """

l = LinkedList()
print("Adding 1...", l.add(1))
print("Adding 2...", l.add(2))
print("Adding 3...", l.add(3))
print("Adding 4...", l.add(4))
print(l, "size -", l.get_size())
print("Removing 4..",l.remove(4))
print("Finding 2...", l.find(2))
print("Removing 2..",l.remove(2))
print("Finding 2...", l.find(2))
print(l, "size -", l.get_size())

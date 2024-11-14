# Imports
from node import Node

# Create your own maze here
# Every node created must be connected to at least 1 node!
A = Node('A')
B = Node('B')
C = Node('C')
D = Node('D')
E = Node('E')
F = Node('F')

A.add_neighbor(B, 2)
A.add_neighbor(D, 8)
B.add_neighbor(D, 5)
B.add_neighbor(E, 6)
D.add_neighbor(E, 3)
D.add_neighbor(F, 2)
E.add_neighbor(F, 1)
E.add_neighbor(C, 9)
F.add_neighbor(C, 3)

A.check_shortest_path(C)

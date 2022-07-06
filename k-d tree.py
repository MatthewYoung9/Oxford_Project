# The aim:
    
    # I've got some random points scattered in an interval.
    # At each step I split the points in two. If the interval is less than
    # delta long then we stop. If the interval has two points in then we stop.
 
import numpy as np

class Node:
    def __init__(self,  points):
        self.points = points
        self.children = []
    @property
    def left_end(self):
        return min(self.points)
    @property
    def right_end(self):
        return max(self.points)
    @property
    def midpoint(self):
        return 0.5*(self.right_end + self.left_end)
    @property
    def width(self):
        return self.right_end - self.left_end
    @property
    def mean(self):
        return np.mean(self.points)
    @property
    def variance(self):
        return np.var(self.points)    
        
def split(node,delta, node_set):
    if node.width > 2*delta and len(node.points) > 2:  # If it's worth splitting then split
        left_child = Node(node.points[node.points <= node.midpoint])  # The points on the left of the midpoint of the subinterval
        right_child = Node(node.points[node.points > node.midpoint])
        node.children.append(left_child)  # To keep track of which intervals have come from where
        node.children.append(right_child)
        node_set.append(left_child)  # Adding the new nodes to the list of nodes
        node_set.append(right_child)
    pass

delta = 0.05
data = np.array([0,1,2,4,5,8,9,12])  # Just as an easy example that can be checked by hand

node_set = [Node(data)]  # Initialise the nodes with the starting interval

for node in node_set:
    split(node,delta, node_set)   # Iteratively split up all intervals that are created
    
compressed = []
for node in node_set:
    if node.children == []:
        compressed.append(node)   # Find the sub-intervals that don't contain other sub intervals


for node in compressed:
    print(node.mean, node.variance)
    
    
    







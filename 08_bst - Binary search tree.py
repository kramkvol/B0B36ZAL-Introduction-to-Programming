class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None
 
class BinarySearchTree:
  def __init__(self):
    self.root = None
    self.visited = 0
 
  def insert(self, value):
    if self.root is None:
        self.root = Node(value)
    else:
        self.recursion_for_insertion(value, self.root)
 
  def recursion_for_insertion(self, value, current_node):
    if value < current_node.value:
        if current_node.left is None:
            current_node.left = Node(value)
        else:
            self.recursion_for_insertion(value, current_node.left)
    elif value > current_node.value:
        if current_node.right is None:
            current_node.right = Node(value)
        else:
            self.recursion_for_insertion(value, current_node.right)
 
  def fromArray(self, values):
    for value in values:
        self.insert(value)
 
  def search(self, value):
    self.visited_count = 0
    return self.recursion_for_search(value, self.root)
 
  def recursion_for_search(self, value, current_node):
    if current_node == None:
      return False
    self.visited_count += 1 
    if current_node.value == value:  
      return True
    if value < current_node.value:
      return self.recursion_for_search(value, current_node.left)
    if value > current_node.value:
      return self.recursion_for_search(value, current_node.right)
 
  def min(self):
    if self.root == None:
        return None
    self.visited_count = 1
    current_node = self.root
    while current_node.left is not None:
        current_node = current_node.left
        self.visited_count += 1
    return current_node.value
 
  def max(self):
    if self.root == None:
        return None
    self.visited_count = 1
    current_node = self.root
    while current_node.right is not None:
        current_node = current_node.right
        self.visited_count += 1
    return current_node.value
 
  def visitedNodes(self):
    return self.visited_count
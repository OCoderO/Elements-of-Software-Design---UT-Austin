#  File: TestBinaryTree.py
#  Description:
#  Student Name: Rosemary Cramblitt
#  Student UT EID: rkc753
#  Partner Name: Wendy Zhang
#  Partner UT EID: wz4393
#  Course Name: CS 313E
#  Unique Number: 52240
#  Date Created: 4/24/21
#  Date Last Modified: 4/26/21

import sys

class Node (object):
  def __init__ (self, data):
    self.data = data
    self.lchild = None
    self.rchild = None

class Tree (object):
  def __init__ (self):
    self.root = None

  # insert a node in a tree
  def insert (self, value):
    #1st create a Node of the value
    new_node = Node (value)

    #Check if tree is empty, if so the node you just created is the root
    if (self.root == None):
      self.root = new_node

    #If the tree is not empty
    else:
      #Create variables to keep track of where we are in the list
      current = self.root
      parent = self.root

      #Check to make sure you have not reached the end of the tree
      while (current != None):
        parent = current

        #Check to see where you need to add it 
        if (value < current.data):
          current = current.lchild
        else:
          current = current.rchild
      #insert the node
      if (value < parent.data):
        parent.lchild = new_node
      else:
        parent.rchild = new_node

  # Returns true if two binary trees are similar
  def is_similar (self, pNode):
    #rename the root of self and pNode 
    a_node = self.root
    b_node = pNode.root
    #Call the helper function
    return self.check_Nodes(a_node, b_node)
    
  #Helper function for is_similar
  def check_Nodes(self, a_node, b_node):
    #Check to see if both trees are empty
    if a_node == None and b_node == None:
      return True
    #Check if only 1 of the trees is empty
    if a_node == None and b_node != None:
      return False
    #Check if only 1 of the trees is empty
    elif a_node != None and b_node == None:
      return False
    #Both trees are not empty, check if the roots are similar
    elif a_node.data != b_node.data:
      return False
    #Traverse through the list checking each node
    else:
      return self.check_Nodes(a_node.lchild, b_node.lchild) and \
      self.check_Nodes(a_node.rchild, b_node.rchild)
      
    

  # Returns a list of nodes at a given level from left to right
  def get_level (self, level): 
    nodes = []
    #Check if level is zero, check if the root != NOne then append to nodes and return
    if level == 0:
      if self.root != None:
        nodes.append(self.root)
      return nodes

    #Call the helper function
    self.get_level_helper(level, 0, nodes, self.root)

    #returns the list
    return nodes

  # Helper for get_level
  def get_level_helper(self, level, current_lvl, nodes_list, temp_Node):
    #if current_lvl > level then we have gone out of bounds and need to return
    if current_lvl > level:
      return
    
    #Check if the tree is empty
    if temp_Node == None:
      return

    #Tree is not empty
    else:
      #Check if you have rached the end of the Tree
      if current_lvl == level:
        nodes_list.append(temp_Node)
      #Traverse through the Tree
      else:
        self.get_level_helper(level, current_lvl + 1, nodes_list, temp_Node.lchild)
        self.get_level_helper(level, current_lvl + 1, nodes_list, temp_Node.rchild)
    

  # Returns the height of the tree
  def get_height (self): 
    #Check if the tree is empty
    if self.root == None:
      return 0
    #Tree is not empty, call helper function
    else:
      return self.get_real_height(self.root)
      
  # returns value height of the tree
  def get_real_height(self, node):
    #Check if node is empty
    if node == None:
      return 0
    #If node is NOT empty add 1 and recursion
    else:
      return 1 + max(self.get_real_height(node.lchild),self.get_real_height(node.rchild))


  # Returns the number of nodes in the left subtree and
  # the number of nodes in the right subtree and the root
  def num_nodes (self):
    #Check if the tree is empty
    if self.root == None:
      return 0
    #If not empty call the helper function
    else:
      return (self.num_nodes_helper(self.root))

  #Helper function that's recursive
  def num_nodes_helper(self,rt):
    #Check if the tree is empty
    if (rt == None):
      return 0
    #If node is NOT empty add 1 and recursion
    else:
      return (self.num_nodes_helper(rt.lchild)+1+self.num_nodes_helper(rt.rchild))


#DEBUGGING PURPOSES
#   def print_tree(self):
#     self.print_tree_helper(self.root, 0)
  
#   def print_tree_helper(self, a_node, space):
#     if a_node != None:
#       space += SPACE
#       self.print_tree_helper(a_node.rchild, space)
#       print()
#       for i in range(SPACE, space):
#         print(end = " ")
#       print(a_node.data)
#       self.print_tree_helper(a_node.lchild, space)

# SPACE = 5 
# self.print_tree()  

def main():
  # Create three trees - two are the same and the third is different
	line = sys.stdin.readline()
	line = line.strip()
	line = line.split()
	tree1_input = list (map (int, line)) 	# converts elements into ints

	line = sys.stdin.readline()
	line = line.strip()
	line = line.split()
	tree2_input = list (map (int, line)) 	# converts elements into ints

	line = sys.stdin.readline()
	line = line.strip()
	line = line.split()
	tree3_input = list (map (int, line)) 	# converts elements into ints

  # Test your method is_similar()

  # Print the various levels of two of the trees that are different

  # Get the height of the two trees that are different

  # Get the total number of nodes a binary search tree

if __name__ == "__main__":
  main()



#  File: ExpressionTree.py
#  Description:
#  Student Name: Rosemary Cramblitt
#  Student UT EID: rkc753
#  Partner Name: Wendy Zhang
#  Partner UT EID: wz4393
#  Course Name: CS 313E
#  Unique Number: 52240
#  Date Created: 4/17/21
#  Date Last Modified: 4/19/21

import sys

operators = ['+', '-', '*', '/', '//', '%', '**']

class Stack (object):
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append (data)

    def pop(self):
        if(not self.is_empty()):
            return self.stack.pop()
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0

class Node (object):
    def __init__ (self, data = None, lChild = None, rChild = None):
        self.data = data
        self.lChild = lChild
        self.rChild = rChild

class Tree (object):
    def __init__ (self):
        self.root = Node(None)
    
    # this function takes in the input string expr and 
    # creates the expression tree
    def create_tree (self, expr):
      # Assume that the expression string is valid and there are spaces between the operators, operands, and the parentheses.
      #Take the expression string and break it into tokens, split where there is empty space
      expression = expr.split()
      new_stack = Stack()
      
      #Start with an empty node, that is the root node, call it the current node
      current_node = self.root
      
      #4 types of tokens - left parenthesis, right parenthesis, operator, and operand
      for token in expression:
        #If the current token is a left parenthesis add a new node as the left child of the current node. Push current node on the stack and make current node equal to the left child.
        if token == '(':
          new_stack.push(current_node)
          current_node.lChild = Node(None)
          current_node = current_node.lChild
     
        #If the current token is an operator set the current node's data value to the operator. Push current node on the stack. Add a new node as the right child of the current node and make the current node equal to the right child.
        elif token in operators:
          current_node.data = token
          new_stack.push(current_node)
          current_node.rChild = Node(None)
          current_node = current_node.rChild

        #If the current token is an operand, set the current node's data value to the operand and make the current node equal to the parent by popping the stack.
        elif token.isdigit() or '.' in token:
          current_node.data = token
          current_node = new_stack.pop()
      
        #If the current token is a right parenthesis make the current node equal to the parent node by popping the stack if it is not empty.
        elif token == ')':
          if not new_stack.is_empty():
            current_node = new_stack.pop()
        else:
          break
    
    # this function should evaluate the tree's expression
    # returns the value of the expression after being calculated
    def evaluate (self, aNode):
      #operators = ['+', '-', '*', '/', '//', '%', '**']
      if aNode.data == '+':
        return float(self.evaluate(aNode.lChild) + self.evaluate(aNode.rChild))

      elif aNode.data == '-':
        return float(self.evaluate(aNode.lChild) - self.evaluate(aNode.rChild))

      elif aNode.data == '*':
        return float(self.evaluate(aNode.lChild) * self.evaluate(aNode.rChild))

      elif aNode.data == '/':
        return float(self.evaluate(aNode.lChild) / self.evaluate(aNode.rChild))
      
      elif aNode.data == '//':
        return float(self.evaluate(aNode.lChild) // self.evaluate(aNode.rChild))
      
      elif aNode.data == '%':
        return float(self.evaluate(aNode.lChild) % self.evaluate(aNode.rChild))

      elif aNode.data == '**':
        return float(self.evaluate(aNode.lChild) ** self.evaluate(aNode.rChild))
    
      elif aNode.data.isdigit() or '.' in aNode.data:
        return eval(aNode.data)
    
    # this function should generate the preorder notation of 
    # the tree's expression
    # returns a string of the expression written in preorder notation
    def pre_order (self, aNode):
      #make sure the list is not empty
      if (aNode.lChild == None) and (aNode.rChild == None):
        return aNode.data
      #for preorder, check and add to str firsrt: center, left, right
      else:
        return aNode.data + " "+ self.pre_order(aNode.lChild) + " " + self.pre_order(aNode.rChild)
       

    # this function should generate the postorder notation of 
    # the tree's expression
    # returns a string of the expression written in postorder notation
    def post_order (self, aNode):
      #make sure list is not empty
        if (aNode != None):
          #create nodelist
          node = ""
          node+=str(self.post_order(aNode.lChild))
          node+=str(self.post_order(aNode.rChild))
          storeddata=aNode.data
          #for preorder, add first then check and add to str: left, right, center
          if storeddata!=None:
            node+=str(aNode.data)+ " "
          return node
        return ""

# you should NOT need to touch main, everything should be handled for you
def main():
    # read infix expression
    line = sys.stdin.readline()
    expr = line.strip()
 
    tree = Tree()
    tree.create_tree(expr)
    
    # evaluate the expression and print the result
    print(expr, "=", str(tree.evaluate(tree.root)))

    # get the prefix version of the expression and print
    print("Prefix Expression:", tree.pre_order(tree.root).strip())

    # get the postfix version of the expression and print
    print("Postfix Expression:", tree.post_order(tree.root).strip())

if __name__ == "__main__":
    main()

# Prefix Expression: * + 8 3 - 7 2
# Postfix Expression: 8 3 + 7 2 - *


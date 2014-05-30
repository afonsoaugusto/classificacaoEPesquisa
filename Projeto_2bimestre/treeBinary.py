# -*- coding: utf-8 -*-
#https://gist.github.com/thinkphp/1450738#file-gistfile1-py-L18
from utils import Util
'''
   by Adrian Statescu <adrian@thinkphp.ro>
   Twitter: @thinkphp
   G+     : http://gplus.to/thinkphp
   MIT Style License
'''
'''
   Binary Search Tree
   ------------------
 
   Trees can come in many different shapes, and they can vary in the number of children allowed per node or in the way
   they organize data values within the nodes. One of the most commonly used trees in computer science is the binary tree.
   A binary tree is a tree in which each node can have at most two children. On child is identified as the left child and
   the other as the right child. The topmost node of the tree is known as the root node.It provides the single acccess point
   into the structure. The root node is the only node in the tree that does not have an incoming edge (an edge directed towart it)
   By definition every non=empty tree must have contain a root node.
  
'''
 
class Node:
 
      def __init__(self,info): #constructor of class
 
          self.info = info  #information for node
          self.left = None  #left leef
          self.right = None #right leef
          self.level = None #level none defined
 
      def __str__(self):
 
          return str(self.info) #return as string
 
 
class searchtree:
 
      def __init__(self): #constructor of class
 
          self.root = None
          self.comparacao = 0
          self.troca = 0
          self.util = Util()
 
 
      def create(self,val):  #create binary search tree nodes
 
          self.comparacao += 1
          if self.root == None:
             self.root = Node(val)
             self.troca += 1
 
          else:
             current = self.root
             self.troca += 1
 
             while 1:
 
                 self.comparacao += 1
                 if val < current.info:
 
                   self.comparacao += 1
                   if current.left:
                      current = current.left
                      self.troca += 1
                   else:
                      current.left = Node(val)
                      self.troca += 1
                      break;      
 
                 elif val > current.info:
                    self.comparacao += 1
                 
                    self.comparacao += 1
                    if current.right:
                       self.troca += 1
                       current = current.right
                    else:
                       self.troca += 1
                       current.right = Node(val)
                       break;      
 
                 else:
                    self.comparacao += 1
                    break 
 
      def bft(self): #Breadth-First Traversal
 
          self.root.level = 0 
          queue = [self.root]
          out = []
          current_level = self.root.level
 
          while len(queue) > 0:
                 
             current_node = queue.pop(0)
 
             if current_node.level > current_level:
                current_level += 1
                out.append("\n")
 
             out.append(str(current_node.info) + " ")
 
             if current_node.left:
 
                current_node.left.level = current_level + 1
                queue.append(current_node.left)
                  
 
             if current_node.right:
 
                current_node.right.level = current_level + 1
                queue.append(current_node.right)
                      
                 
          self.util.imprimir(self.util.INFO,"".join(out))   
 
 
      def inorder(self,node):
            
           if node is not None:
              
              self.inorder(node.left)
              self.util.imprimir(self.util.INFO,node.info)
              self.inorder(node.right)
 
 
      def preorder(self,node):
            
           if node is not None:
              
              self.util.imprimir(self.util.INFO,node.info)
              self.preorder(node.left)
              self.preorder(node.right)
 
 
      def postorder(self,node):
            
           if node is not None:
              
              self.postorder(node.left)
              self.postorder(node.right)
              self.util.imprimir(self.util.INFO,node.info)
 
'''Zafir Ahmed Abbasi(19B-122-CS)
Shehroz Ali Khan(19B-128-CS)'''

'''Github Link :https://github.com/zaabbasi/Splay-Tree'''

class Node:
    def __init__(self, value):
      self.value = value
      self.parent = None
      self.left = None
      self.right = None
    
class SplayTree:
    
    def __init__(self):
      self.root = None
    
    
    def leftRotate(self, b):
      a = b.right
      b.right = a.left
      
      if a.left != None:
        a.left.parent = b
    
      a.parent = b.parent
      if b.parent == None:
        self.root = a
    
      elif b == b.parent.left: 
        b.parent.left = a
    
      else: 
        b.parent.right = a
    
      a.left = b
      b.parent = a
    
    def rightRotate(self, b):
        
      a = b.left
      b.left = a.right
      if a.right != None:
        a.right.parent = b
    
      a.parent = b.parent
      if b.parent == None:
        self.root = a
    
      elif b == b.parent.right: 
        b.parent.right = a
    
      else: 
        b.parent.left = a
    
      a.right = b
      b.parent = a
    
    def Splay(self, n):
      while n.parent != None:
        if n.parent == self.root: 
          if n == n.parent.left:
            self.rightRotate(n.parent)
          else:
            self.leftRotate(n.parent)
    
        else:
          p = n.parent #parent of node
          g = p.parent #grandparent of node
    
          if n.parent.left == n and p.parent.left == p: 
            self.rightRotate(g)
            self.rightRotate(p)
    
          elif n.parent.right == n and p.parent.right == p: 
            self.leftRotate(g)
            self.leftRotate(p)
    
          elif n.parent.right == n and p.parent.left == p:
            self.leftRotate(p)
            self.rightRotate(g)
    
          elif n.parent.left == n and p.parent.right == p:
            self.rightRotate(p)
            self.leftRotate(g)
    
    def InsertNode(self, n):
      a = None
      var = self.root #temporary variable
      while var != None:
        a = var
        
        if n.value < var.value:
          var = var.left
          
        else:
           var = var.right
    
      n.parent = a
    
      if a == None: #newly added node is root
        self.root = n
        
      elif n.value < a.value:
        a.left = n
        
      else:
        a.right = n
    
      self.Splay(n)
    
    def SearchNode(self, n, b):
        
      if b == n.value:
        self.Splay(n)
        return n
    
      elif b < n.value:
        return self.SearchNode(n.left, b)
    
      elif b > n.value:
        return self.SearchNode(n.right, b)
    
      else:
         return None
    
    def DeleteNode(self, n):
      
        self.Splay(n)
      
        '''#LeftSubTree'''
    
        l_st = SplayTree()  
        l_st.root = self.root.left
        if l_st.root != None:
            l_st.root.parent = None
            
        '''#RightSubTree'''
        
        r_st = SplayTree() 
        r_st.root = self.root.right
      
        if r_st.root != None:
          r_st.root.parent = None
      
        if l_st.root != None:
          m = l_st.FindMaxNode(l_st.root)
          l_st.Splay(m)
          l_st.root.right = r_st.root
          self.root = l_st.root
      
        else:
          self.root = r_st.root
          
    def FindMaxNode(self, b):
        
      while b.right != None:
        b = b.right
      return b
    
    def Inorder(self, n):
          if n != None:
            self.Inorder(n.left)
            print(n.value)
            self.Inorder(n.right)

tree = SplayTree()

n1 = Node(15)
n2= Node(61)
n3= Node(25)
n4= Node(80)
n5= Node(70)
n6= Node(50)
n7= Node(10)
n8= Node(20)
n9= Node(90)
n10 = Node(150)

tree.InsertNode(n1)
tree.InsertNode(n2)
tree.InsertNode(n3)
tree.InsertNode(n4)
tree.InsertNode(n5)
tree.InsertNode(n6)
tree.InsertNode(n7)
tree.InsertNode(n8)
tree.InsertNode(n9)
tree.InsertNode(n10)

tree.SearchNode(tree.root, 15)
tree.DeleteNode(n1)
tree.DeleteNode(n5)

tree.FindMaxNode(tree.root)
tree.Inorder(tree.root)

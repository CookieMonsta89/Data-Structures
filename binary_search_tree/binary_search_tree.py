class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    #store variables for self as well as a true false
    current = self
    complete = False
    #begin loop using the true false 
    while not complete:
      #here I need to compare values using an if statement
      if current.value > value:
        #check that there is a left branch
        if current.left:
          #if there was a left I need to set the left to the new currentvalue
          current = current.left
        #if there is no left to the node, I'll need to create a new node
        else:
          current.left = BinarySearchTree(value)
          complete = True
      #if the current value was < val go into this condition
      else:
        #check if there is a right, same logic as above
        if current.right:
          current = current.right
        else:
          current.right = BinarySearchTree(value)
          complete = True

  def contains(self, target):
    pass

  def get_max(self):
    pass

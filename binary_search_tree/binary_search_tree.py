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
    current = self
    complete = False

    while not complete:
      #if there is nothing left to check, then return false
      if not current:
        return False
      #if the value of the current node is equal to the target
      if current.value == target:
        return True
      #if the current value is greater than the target
      elif current.value > target:
        current = current.left
      #if current value is less than the target 
      else:
        current = current.right

  def get_max(self):
    current = self
    max = 0

    while current:
      #if the current value is greater than the max
      if current.value > max:
        max = current.value
        current = current.right

    return max

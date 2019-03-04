class Queue:
  def __init__(self):
    self.size = 0
    # what data structure should we
    # use to store queue elements?
    self.storage = []

  def enqueue(self, item):
    self.storage.append(item)
    self.size += 1
    # adds item to the back of the queue
  
  def dequeue(self):
    if self.size == 0:
      return None
    else:
      self.size -= 1
      return self.storage.pop(0)
    # dequeue removes and return an item from the front of the queue

  def len(self):
    return self.size
    # returns the number of the items in the queue

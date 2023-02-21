#Reversão no local de uma lista vinculada
#Lista de links reversos
class Pilha:

  def __init__(self, data=None, next=None):
    self.data = data
    self.next = next

  def push(self, newData=None):
    if newData is None:
      return

    p1 = Pilha(self.data, self.next)

    self.data = newData
    self.next = p1
  
  def pop(self):
    if not self:
      return None
    
    poped = self.data
    
    #if not self.next:
    if self.next is None:
      self.data = None
      self.next = None
    else:
      self.data = self.next.data
      #self.next = None
      self.next = self.next.next
    return poped

  def toArray(self, array=[]):
    if self is None:
      return

    array.append(self.data)

    if self.next is not None and self.next.data is not None:
      self.next.toArray(array)

    return array

  
  def print(self):
    array = self.toArray([])
    print(array)

  def mesclar(self):
    aux = Pilha()
    box = []
    while list_1 is not None:
        f = list_1.pop()
        box.append(f)
        if f is None:
            break
    box.pop()

    while list_2 is not None:
        f = list_2.pop()
        box.append(f)
        if f is None:
            break
        
    box.pop()
    box.sort()
    box.reverse()
    for i in box:
        aux.push(i)
    
    aux.print()
    return


    
if __name__ == "__main__":
  
  mesc = Pilha()
  list_1 = Pilha()
  list_1.push(1)
  list_1.push(3)
  list_1.push(7)
  list_1.push(None)
  list_2 = Pilha()
  list_2.push(3)
  list_2.push(6)
  list_2.push(None)
  
  print(mesc.mesclar())
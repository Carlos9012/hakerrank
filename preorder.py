class NodoArvore: 

  
  def __init__(self, key, dir, esq):
    self.item = key
    self.dir = dir
    self.esq = esq
  
  def printTree(self, level=0):
    if self == None:
      return

    if self.dir is not None:
      self.dir.printTree(level + 1)

    print((' ' * 4 * level) + '-> ' + self.item)
    
    if self.esq is not None:
      self.esq.printTree(level + 1)
    return
    
  
  def preOrder(self, atual):
    if atual != None:
        print(atual.item,end=" ")
        self.preOrder(atual.esq)
        self.preOrder(atual.dir)
    return
  

if __name__ == "__main__":
  G = NodoArvore('G', None, None)
  F = NodoArvore('F', None, None)
  E = NodoArvore('E', None, None)
  D = NodoArvore('D', None, None)
  
  C = NodoArvore('C', F, G)
  B = NodoArvore('B', D, E)

  A = NodoArvore('A', C, B)
  
  A.printTree()
  A.preOrder(A)
  print('Pré-ordem')
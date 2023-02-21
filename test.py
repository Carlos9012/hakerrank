'''Seja S = (s1, s2, ..., sn) uma sequência de números. Dizemos que S’ é uma subsequência de S se é
possível obter S’ a partir de S removendo alguns dos elementos de S.
Ex: S = (8, 4, 9, 3, 4, 7, 5, 10, 3)
(4, 7, 1, 10)
(4, 4, 10, 5)
(8, 3, 7, 10, 3)
Uma subsequência é crescente se os seus elementos estão em ordem crescente.
Ex: (8, 9, 10)
No Problema da Subsequência Crescente Máxima (SCM) é dada uma sequência S e desejamos
encontrar o comprimento de uma subsequência crescente de S que tenha a maior quantidade possível
de elementos.'''

#se for em ordem

#Entrada: uma matriz S com (s1, s2, ...sn) e uma variavel cont = 0
#Saida: o a maior subsequência maxima


S = [8,4,9,3,4,7,5,10,3]
aux = []
p = []
C = [1]
for i in range(0, len(S)):
    elemtnt = 1
    for j in range(0, i-1):
        if S[j] <= S[i] and C[j] + 1 > C[i-1]:
            elemtnt += 1
            aux.append(S[j])
            print(aux)
    aux.clear()
    C.append(elemtnt)

print(max(C))

from random import shuffle

# busca o resultado ótimo percorrendo a sequência em ordem inversa e obtem o ótimo para todos os indices
def otimo_2(sequencia):
    otimos = dict()
    n = len(sequencia) - 1
    while n >= 0:
        valor = sequencia[n]
        subsequencia = [valor]
        for subsequencia_parcial in otimos.values():
            if valor < subsequencia_parcial[0]:
                subsequencia = max([subsequencia, [valor] + subsequencia_parcial], key=lambda x: len(x))
        otimos[n] = subsequencia
        n -= 1
    return max(otimos.values(), key=lambda x: len(x))


'''sequencia_fixa = [19, 1, 17, 18, 2, 15, 16, 3, 13, 14, 4]
print(otimo_2(sequencia_fixa))'''

def scm_PD(s=[]):

  n = len(s)
  c = []
  p = []
  k = 0
  scm = []
  for i in range(0, n):
    c.append(1)
    p.append(1)
    for j in range(i):
      if s[j] <= s[i] and c[j] + 1 > c[i]:
        c[i] = c[j] + 1
        p[i] = j

  k = max(c)
  scm.append(s[k])
  while p[k] != k:
    scm.insert(0, s[p[k]])
    k = p[k]

  return scm

print(scm_PD([8, 2, 9, 3, 4, 7]))

a = 2
b = 3
mul = 1

for i in range(0, b):
  mul *= a

print(mul)

aux = a**(int((b-1)/2))
if a%2==0:
  print(aux*aux)
else:
  print(aux*aux*a)

  
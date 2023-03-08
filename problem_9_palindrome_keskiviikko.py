numero = 12321

numerolista = [int(x) for x in str(numero)]
kaannetty_lista = []

class Solution:
  def __init__(self):
    self.numerolista = []
    self.tulos = 0

  def palindrome(self, number):
    print(numerolista)
    for i, x in reversed(list(enumerate(numerolista))):
        kaannetty_lista.append(x)
    print(kaannetty_lista)
    if numerolista == kaannetty_lista:
      return True
    else:
      return False
        
          
      

ratkaisu = Solution()

lopullinen_vastaus = ratkaisu.palindrome(numerolista)

print(lopullinen_vastaus)
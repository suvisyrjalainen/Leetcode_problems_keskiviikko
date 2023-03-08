nums = [5,7,3,5]
target = 10

class Solution:
  def __init__(self):
    self.numerolista = []
    self.tulos = 0

  def twosum(self, lista, summa):
    self.numerolista = lista
    self.tulos = summa
    for x in lista:
      for y in lista:
        if x + y == summa and lista.index(x) != lista.index(y):
          return [lista.index(x), lista.index(y)]
      

ratkaisu = Solution()

lopullinen_vastaus = ratkaisu.twosum(nums, target)

print(lopullinen_vastaus)
matriz1 = [[1, 1, 1, 3],[2, 2, 2, 7],[3, 3, 3, 9],[4, 4, 4, 13]]

def sum(matriz):
  suma = 0
  for fila in matriz:
      for elemento in fila:
          suma += elemento
  print(suma)

sum(matriz1)


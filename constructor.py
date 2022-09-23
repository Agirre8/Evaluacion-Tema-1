matriz = [[1, 1, 1, 3],[2, 2, 2, 7],[3, 3, 3, 9],[4, 4, 4, 13]]

def sum(matriz, suma):

  suma = 0
  for fila in matriz:
      for elemento in fila:
          suma += elemento

        
def cadena_texto(texto):
  texto= input("introduzca una palabra")
  longitud = len(texto)
  if int(3) <= longitud < int(10):
    return True
  else:
     return False

def lista_numeros_1 ():
  list(range(n+1))

def lista_numeros_2 ():
  list(range(-10, 1))

def lista_numeros_3 ():
  list(range(0, 21, 2))

def lista_numeros_4 ():
  list(range(-19, 1, 2))

def lista_numeros_5 ():
  list(range(0, 51, 5))

cadena_texto("hola")
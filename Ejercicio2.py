
def cadena_texto(texto):
  texto= input("introduzca una palabra")
  longitud = len(texto)
  if int(3) <= longitud < int(10):
    return True
  else:
     return False

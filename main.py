
def sumacuadrado(n):
  operaciones=0
  resultado=0
  print("n Resultado Operaciones")
  for i in range(1,n+1):
    resultado=(i*i)+resultado
    operaciones+=1 #sumar una operacion multiplicacion
    if(i>1):
      operaciones+=1 #sumar una operacion suma
    print(i,"   ",resultado,"   ",operaciones)

def sumacuadradoerror(n):
  cuatro=0
  cinco=0
  diez=0
  cuatrot=0
  cincot=0
  diezt=0
  cuatrot2=0
  cincot2=0
  diezt2=0
  resultado1=0
  print(" ")
  print("Prueba Teorica(Sin Error)")
  print("n   Resultado")
  for i in range(1,n+1):
    resultado1=(i*i)+resultado1
    print(i,"   ",resultado1)
    if i == 4:
      cuatro=resultado1
    if i == 5:
      cinco=resultado1
    if i == 10:
      diez=resultado1
  print(" ")
  print("Experimento (Suma error 0.1)")
  print("n    Resultado")
  resultado=0
  for i in range(1,n+1):
    i=i+0.1
    resultado=(i*i)+resultado
    print(i,round(resultado,16))
    if i == 4.1:
      cuatrot=resultado
    if i == 5.1:
      cincot=resultado
    if i == 10.1:
      diezt=resultado
  print(" ")
  print("Experimento (Resta error 0.1)")
  print("n    Resultado")
  resultado2=0
  for i in range(1,n+1):
    i=i-0.1
    resultado2=(i*i)+resultado2
    print(i,round(resultado2,16))
    if i == 3.9:
      cuatrot2=resultado2
    if i == 4.9:
      cincot2=resultado2
    if i == 9.9:
      diezt2=resultado2

  e1=((abs(cuatro-cuatrot))/cuatro)*100
  e2=((abs(cuatro-cuatrot2))/cuatro)*100
  print(" ")
  print("ERROR RELATIVO PARA n=4")
  print("  Valor teorico: ",cuatro)
  print("  Valor Experimental(+0.1): ",cuatrot)
  print("  Error Relativo: ",e1,"%")
  print("  Valor Experimental(-0.1): ",cuatrot2)
  print("  Error Relativo",e2,"%")
  e1=((abs(cinco-cincot))/cinco)*100
  e2=((abs(cinco-cincot2))/cinco)*100
  print(" ")
  print("ERROR RELATIVO PARA n=5")
  print("  Valor teorico: ",cinco)
  print("  Valor Experimental(+0.1): ",cincot)
  print("  Error Relativo: ",e1,"%")
  print("  Valor Experimental(-0.1): ",cincot2)
  print("  Error Relativo",e2,"%")
  e1=((abs(diez-diezt))/diez)*100
  e2=((abs(diez-diezt2))/diez)*100
  print(" ")
  print("ERROR RELATIVO PARA n=10")
  print("  Valor teorico: ",diez)
  print("  Valor Experimental(+0.1): ",diezt)
  print("  Error Relativo: ",e1,"%")
  print("  Valor Experimental(-0.1): ",diezt2)
  print("  Error Relativo",e2,"%")
  
def menu():
  menu=-1
  while menu != 0:
    print("***SUMAR LOS PRIMERO NUMEROS NATURALES AL CUADRADO***")
    print("  1.Imprimir varias pruebas para varios valores de n")
    print("  2.Error relativo para n=4,5,10")
    print("  0.Salir")
    menu=int(input("Ingrese una opcion: "))
    print(" ")
    if(menu == 1):
      sumacuadrado(100)
      print(" ")
    if(menu == 2):
      sumacuadradoerror(10)
      print(" ")
menu()

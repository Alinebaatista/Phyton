            # WHILE -- ENQUANTO
  
import os
import time


contador = 0
while(contador < 5 ):
  print(contador)
  contador = contador + 1

              #While-else 

contador = 0 # variavel se inicia com um valor
while(contador < 5 ):
  print(contador) # mostra o valor na tela
  contador = contador + 1 # faz com que conte até o número desejado

else:
  print('O loop while foi encerrado com sucesso!')

  
              #while - IF- else

  input('Digite um número:')
input = 0
while input < 10 :
  print(input)
  input += 1
  if input == 6:
    print("x é igual a 6")
    break
  else:
    print("Fim while")
    
  
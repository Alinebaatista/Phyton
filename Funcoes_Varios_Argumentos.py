
#XARGS = Varios argumentos

def soma(*numeros): # * = Define que vou receber varios arumentos dentro da função
  return numeros
  
x = soma(2,3,4,5)
print(x)

#Função soma com xargs utilizando o loop
#Soma
def soma(*numeros):
  r = 0
  for num in numeros:
    r += num
  return r
  
x = soma(2,3,4,5)
print(x)


#Subtração
def soma(*numeros):
  r = 0
  for num in numeros:
    r -= num
  return r
  
x = soma(2,3,4,5)
print(x)


#Multiplicação
def soma(*numeros):
  r = 0
  for num in numeros:
    r *= num
  return r
  
x = soma(2,3,4,5)
print(x)


#Divisão
def soma(*numeros):
  r = 0
  for num in numeros:
    r /= num
  return r
  
x = soma(2,3,4,5)
print(x)

#Função com varios argumentos de diferentes tipos de dados

def agencia(**carro):
  return carro
  
print(agencia(modelo='Palio', cor='prata', ano= 2013, motor= 1.0))




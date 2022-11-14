                  #       LISTA

lista = [] # vazia 
lista 
[]

lista = ["o Carro", 'o peixe', 123,111]  # 4 indices

lista
["o Carro", 
  'o peixe',
  123,
  111
]


nova_list = ['pedra', lista]# colocar uma list adentro de outra

print(lista)
print(nova_list)


print(lista[2]) # ele inicia no zero ou seja mostrar 123 

print(lista + nova_list)
print( lista*3)

print()

# validar
print("peixe" in lista)
print("gato" in lista)

print()

# colocar números e mostrar a soma , maior e menor número
numeros =[6,8,12,53,14,78]

print(min(numeros))
print(max(numeros))
print(sum(numeros))

print("---------------------------------------------")

print("Digite 5 Nomes :")

nome1=str(input("Digite 1 Nome :"))
nome2=str(input("Digite  2 Nome :"))
nome3=str(input("Digite 3 Nome :"))
nome4=str(input("Digite 4 Nome :"))
nome5=str(input("Digite 5 Nome :"))

listaN=[nome1,nome2,nome3,nome4,nome5]


print("\t Digite 5 Idades ")

idade1=str(input("Digite 1 Idade :"))
idade2=str(input("Digite  2 Idade :"))
idade3=str(input("Digite 3 Idade :"))
idade4=str(input("Digite 4 Idade :"))
idade5=str(input("Digite 5 Idade :"))

listaI=[idade1,idade2,idade3,idade4,idade5]


print("o mais novo tem : " + min(listaI))
print("o mais velho tem : " + max(listaI))




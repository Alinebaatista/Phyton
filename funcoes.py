                      #FUNCTION:
#Faz com que seja executado um mesmo grupo de código várias vezes dentro de um programa. 
#F= print formatdao
#DRY - Don't repet Yourself


def boas_vindas():
  print("Olá Maria temos 5 laptops ")
  print("Disponiveis")

boas_vindas()

print("----------------------------------------------------------")
      #Variaveis dentro da função

def soma_numeros():
  n1=5
  n2=10
  result=n1+n2 #variavel privada
  print(result)

soma_numeros()



print("------------------------------------------------------------------")
      #Parametros dentro da função / input na função

def atributos(nome,quantidade):
  print(f' Ola,{nome}')
  print(f'temos {str(quantidade)} laptops em estoque ')

atributos("Aline",20)

atributos(nome=input('Digite o nome do cliente : '),quantidade=input("Digite a quantidade :"))



print("-----------------------------------------------------------------")

                #Parametro Padrão-valores pré estabelecido ,por padrão um argumento non default vem                          #primeiro,antes do default
def boas_vindas(nome,quantidade=8):
  print(f' Ola,{nome}')
  print(f'temos {quantidade} laptops em estoque ')


boas_vindas("Aline")



print("-----------------------------------------------------------------")
                #PRINT & RETURN 
#PRINT:Realiza uma tarefa,
#RETURN:Calcula e retorna um valor,guarda o valor na memoria para reutilizaçõa

def cliente1(nome):
  print(f'ola {nome}')

cliente1("Aline")

def cliente12(nome):
  return F'ola {nome}'







































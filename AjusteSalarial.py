#Reajuste salario
print("\t --- Ajuste Salárial --- ")

nome = str(input (" Digite o Nome : "))
idade = int(input (" Digite a idade :"))
cpf = int(input (" Digite o CPF : "))
salario = float (input (" Digite o atual salário : "))

if salario < 500:# ( : )faca
  reajuste = salario+(salario*0.15)
  print("\n O seu salário foi reajustado para 15% de acresimo " , reajuste) 
  
elif salario >= 1000:
  reajuste = salario+(salario*0.05)
  print("\n O seu salário foi reajustado para 5% de acresimo " ,reajuste)

elif salario > 500 and salario < 1000:
   reajuste = salario+(salario*0.10)
   print("\n O seu salário foi reajustado para 10% de acresimo " ,reajuste)

 








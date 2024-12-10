#bloco 1 -------------------- 
# Solicita ao usuário informe o tipo de equação que ele quer utilizar.
print("Escolha a equação matemática que deseja realizar:")
lista = ['1 para Somar;', '2 para Subtrair;', '3 para Dividir;', '4 para Multiplicar;','5 para sair.']
print("\n".join(lista))
equacao = input("Digite aqui:")

#bloco 2 --------------------
#Pede para o usuário inserir um opção válida,  caso não tenha colocado
desc_eq = ""
tipo = ""
while int(equacao) > 5 or int(equacao) < 1:
    if int(equacao) > 5 or int(equacao) < 1 :  
      print('\033[35mDigite um valor válido de 1 a 5:\033[0m')
      print("\n".join(lista))
      equacao = input("Digite aqui:")

#bloco 3 --------------------
#Trabalha os calculos exceto Divisão
if int(equacao) <= 4:
  print('\033[32mVálido!\033[0m')
  if int(equacao) != 3:
    print('Digite o primeiro valor numérico:') 
    x = int(input())
    print('Digite o Segundo valor numérico:') 
    y = int(input())

    if int(equacao) == 1:
      txt = 'Soma'
      result = x + y
      msg = "Soma = ", result
    if int(equacao) == 2:
      txt = 'Subtração'
      result = x - y
      msg = "Subtração = ", result
    if int(equacao) == 4:
      txt = 'Multiplicação'
      result = x * y
      msg = "Multiplicação = ", result

#bloco 3 --------------------
#Trabalha os calculos para Diviisão      
  if int(equacao) == 3:
    x = 0
    while int(x) < 1:
      print('\033[34mLembre-se que para duvisão o valor deve ser maior que zero!\033[0m')
      print('Digite o primeiro valor numérico:') 
      x = int(input())
      
    print('Digite o Segundo valor numérico:') 
    y = int(input()) 
           
    txt = 'Divisão'
    result = x / y
    msg = "Multiplicação = ", result 

#bloco 4 --------------------
#Apresenta o resultado caso esteja tudo certo
  print('Resultado da', txt,'=', float(result))


#bloco 5 --------------------
#informa ao usuário que ele optou por sair escolhendo a opção 5
if int(equacao) == 5:
  print('\033[35mVocê optou por sair!\033[0m')

  

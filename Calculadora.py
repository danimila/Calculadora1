#bloco 1 -------------------- 
# Solicita ao usuário informe o tipo de equação que ele quer utilizar.
print("Escolha a equação matemática que deseja realizar:")
lista = ['Digite 1 para Somar;', 'Digite 2 para Subtrair;', 'Digite 3 para Dividir;', 'Digite 4 para Multiplicar.']
print("\n".join(lista))
equacao = input("Digite aqui:")


#bloco 2 --------------------
#Verifica, valida e informa ao usuário a equação que ele selecionou
desc_eq = ""
tipo = ""
if int(equacao) == 1:
  desc_eq = "Você optou por Somar!"
  tipo = "Somar"
  print(desc_eq)
if int(equacao) == 2:
  desc_eq = "Você optou por Subtrair!"
  tipo = "Subtrair"
  print(desc_eq)
if int(equacao) == 3:
  desc_eq = "Você optou por Dividir!"
  tipo = "Dividir"
  print(desc_eq)
if int(equacao) == 4:
  desc_eq = "Você optou por Multiplicar!"
  tipo = "Multiplicar"
  print(desc_eq)
if int(equacao) > 4:
  desc_eq = "Erro!! - Você precisa digitar uma equação válida!"
  print("\033[31m", desc_eq,"\033[0m")
  vlr1 = 0
  while int(equacao) > 4:
    desc_eq = "Erro!! - Você precisa digitar uma equação válida!"
    print("\033[31m", desc_eq,"\033[0m")
    print("\n".join(lista))
    equacao = input("Digite aqui:")

    try:
      if int(vlr1) == int:
        vlr1 = int(vlr1)
    except:
        vlr1 = 0
        print("\033[31mO valor digitado precisa ser um número!\033[0m")

  print("\033[32mVálido!\033[0m")

#bloco 3 --------------------
#Solicita ao usuário o primeiro valor da equção e verifica se é um valor válido
vlr1 = 0
vlr1 = input("Digite o primeiro valor:")

while isinstance(vlr1, str):
    try:
      if isinstance(int(vlr1), int):
        if int(equacao) < 3:
          vlr1 = int(vlr1)
          print("\033[32mVálido!\033[0m")
        else:
          if int(equacao) > 2 and int(vlr1) > 0:
            vlr1 = int(vlr1)
            print("\033[32mVálido!\033[0m")
          else:
            print("\033[31mPara este tipo de equação valor tem que ser maior que zero!\033[0m")
            vlr1 = input("Digite o primeiro valor:")
    except:
        print("\033[31mDigite um valor numérico!\033[0m")
        vlr1 = input("Digite o primeiro valor:")

#bloco 4 --------------------
#Solicita ao usuário o segundo valor da equção e verifica se é um valor válido
vlr2 = 0
vlr2 = input("Digite o primeiro valor:")

while isinstance(vlr2, str):
    try:
      if isinstance(int(vlr2), int):
        if int(equacao) < 3:
          vl2 = int(vlr2)
          print("\033[32mVálido!\033[0m")
        else:
          if int(equacao) > 2 and int(vlr2) > 0:
            vlr2 = int(vlr2)
            print("\033[32mVálido!\033[0m")
          else:
            print("\033[31mPara este tipo de equação valor tem que ser maior que zero!\033[0m")
            vlr2 = input("Digite o primeiro valor:")
    except:
        print("\033[31mDigite um valor numérico!\033[0m")
        vlr2 = input("Digite o primeiro valor:")

#bloco 5 --------------------
#Realiza a equação considerando a escolhida
if int(equacao) == 1:
  result = vlr1 + vlr2
if int(equacao) == 2:
  result = vlr1 - vlr2
if int(equacao) == 3:
  result = vlr1 / vlr2
if int(equacao) * 3:
  result = vlr1 / vlr2

#bloco 6 --------------------
#Apresenta o resultado
print("Ao", tipo, "os valores apresentados encontrei o seguinte resultado:")
print(float(result))
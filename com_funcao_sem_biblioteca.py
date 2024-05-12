#calculadora com função e sem biblioteca
# calculadora binaria : a.	Conversão de decimal para binário, hexadecimal e octal. 
# b.	Conversão de binário, hexadecimal e octal para decimal. 


def decimal_binario() :
    #decimal para binario
    decimal = int(input("Digite um número decimal: "))
    binario = ""
    while decimal > 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2
    print("\na conversão de decimal para binario : ", binario)

def decimal_hexadecimal() : 
    #decimal para hexadecimal 
   decimal = int(input("Digite um número decimal : "))
   hexadecimal = ""
   while decimal > 0:
       resto = decimal % 16
       if resto < 10:
           hexadecimal = str(resto) + hexadecimal
       else:
           hexadecimal = chr(resto + 55) + hexadecimal
       decimal = decimal // 16

   print("\na conversão de decimal para hexadecimal é : ", hexadecimal)

def decimal_octal() :
    #decimal para octal
    decimal = int(input("Digite um numero decimal : "))
    octal = ""
    while decimal > 0:
         resto = decimal % 8
         octal = str(resto) + octal
         decimal = decimal // 8

    print("\na conversão de decimal para octal: ", octal)

def binario_decimal() :
    #binario para decimal 
    binario = input("Digite um numero binario : ")
    decimal = 0
    potencia = len(binario) - 1
    for digito in binario:
       decimal += int(digito) * (2 ** potencia)
       potencia -= 1
    print("\na conversão de binario para decimal é : ", decimal)


def hexadecimal_decimal() :
    #hexadecimal para decimal
  hexadecimal = input("Digite um numero hexadecimal(caso possua letras, digite em maiusculo) : ")
  decimal = 0
  potencia = len(hexadecimal) - 1
  for digito in hexadecimal:
      if digito.isdigit():
          decimal += int(digito) * (16 ** potencia)
      else:
          decimal += (ord(digito) - 55) * (16 ** potencia)
      potencia -= 1
  print("\na conversão de hexadecimal para decimal é: ", decimal)

def octal_decimal() :
    #octal para decimal 
  octal = input("Digite um numero octal : ")
  decimal = 0
  potencia = len(octal) - 1
  for digito in octal:
      decimal += int(digito) * (8 ** potencia)
      potencia -= 1
  print("\na conversão de octal para decimal é : ", decimal)

def main() : 
  while True :
    print("\nEscolha o numero da conevrsão desejada: ")
    print("1. Decimal para binário")
    print("2. Decimal para hexadecimal")
    print("3. Decimal para octal")
    print("4. Binário para decimal")
    print("5. Hexadecimal para decimal")
    print("6. Octal para decimal")
    print("0. Sair")

    opcao = int(input("\nDigite o número da opção desejada: "))
    if opcao == 1:
       decimal_binario()
    elif opcao == 2:
         decimal_hexadecimal()
    elif opcao == 3 :
         decimal_octal()
    elif opcao == 4 :
         binario_decimal()
    elif opcao == 5 :
         hexadecimal_decimal()
    elif opcao == 6 :
         octal_decimal()
    elif opcao == 0 :
         print("\nencerrando o programa...")
         break
    else :
         print("\nOpção inválida. Digite uma opção de 1 a 6 ou 0 para sair.")

if __name__ == "__main__":
   main()
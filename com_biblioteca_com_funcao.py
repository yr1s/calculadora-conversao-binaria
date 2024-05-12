#calculadora binaria : a.	Conversão de decimal para binário, hexadecimal e octal. 
# b.	Conversão de binário, hexadecimal e octal para decimal. 
#calculadora com função e biblioteca

def decimal_para_binario():
    decimal = int(input("Digite o número decimal: "))
    return bin(decimal)[2:]  # Remove os dois primeiros caracteres

def decimal_para_hexadecimal():
    decimal = int(input("Digite o número decimal: "))
    return hex(decimal)[2:]  # Remove os dois primeiros caracteres

def decimal_para_octal():
    decimal = int(input("Digite o número decimal: "))
    return oct(decimal)

def binario_para_decimal():
    binario = input("Digite o número binário: ")
    return int(binario, 2)[2:]  # Remove os dois primeiros caracteres

def hexadecimal_para_decimal():
    hexadecimal = input("Digite o número hexadecimal: ")
    return int(hexadecimal, 16)[2:]  # Remove os dois primeiros caracteres

def octal_para_decimal():
    octal = input("Digite o número octal: ")
    return int(octal, 8)[2:]  # Remove os dois primeiros caracteres



def main():
    while True:
        print("Escolha a operação desejada:")
        print("1. Conversão de decimal para binário")
        print("2. Conversão de decimal para hexadecimal")
        print("3. Conversão de decimal para octal")
        print("4. Conversão de binário para decimal")
        print("5. Conversão de hexadecimal para decimal")
        print("6. Conversão de octal para decimal")
        print("0. Sair")
        
        escolha = input("Digite o número da operação desejada: ")

        if escolha == "0":
            print("Encerrando o programa...")
            break
        elif escolha == "1":
            print("Binário:", decimal_para_binario())
        elif escolha == "2":
            print("Hexadecimal:", decimal_para_hexadecimal())
        elif escolha == "3":
            print("Octal:", decimal_para_octal())
        elif escolha == "4":
            print("Decimal:", binario_para_decimal())
        elif escolha == "5":
            print("Decimal:", hexadecimal_para_decimal())
        elif escolha == "6":
            print("Decimal:", octal_para_decimal())
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()

import Cifra_node

def main():
    opcao = input("Escolha uma opção:\n1. Cifrar mensagem\n2. Decifrar mensagem\nDigite o número da opção desejada: ")
    chave = input("Digite a chave: ")
    mensagem = input("Digite a mensagem: ")

    cifra = Cifra_node.Cifra_de_Vigenere(chave)
    if opcao == "1":
        print("Mensagem cifrada:", cifra.cifragem(mensagem))
    elif opcao == "2":
        print("Mensagem original:", cifra.decifragem(mensagem))
    else:
        print("Opção inválida.")

if __name__ == "__main__":
    main()
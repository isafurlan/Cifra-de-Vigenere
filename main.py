import Cifra_node

def main():
    chave = input("Digite a chave: ")
    mensagem = input("Digite a mensagem: ")

    cifra = Cifra_node.Cifra_de_Vigenere(chave)
    mensagem_cifrada = cifra.cifragem(mensagem)

    print("Mensagem cifrada:", mensagem_cifrada)


if __name__ == "__main__":
    main()
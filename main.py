import Cifra_Decifra_Vigenere

def main():        
    chave = input("Digite a chave: ")                                       # Solicita a chave ao usuário.    
    mensagem = input("Digite a mensagem: ")                                 # Solicita a mensagem ao usuário.    
                  
    cifra = Cifra_Decifra_Vigenere.Cifra_e_Decifra_de_Vigenere(chave)       # Cria o objeto da Cifra de Vigenère.
    mensagem_cifrada = cifra.cifragem(mensagem)                             # Realiza a cifragem da mensagem.    
    print("\nMensagem cifrada:", mensagem_cifrada)                          # Mostra a mensagem cifrada.

    mensagem_decifrada = cifra.decifragem(mensagem_cifrada)                 # Realiza a decifragem do criptograma.    
    print("Mensagem decifrada:", mensagem_decifrada)                        # Mostra a mensagem recuperada.


if __name__ == "__main__":
    main()
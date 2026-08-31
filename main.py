import Cifra_Decifra_Vigenere
import Criptoanalise_Vigenere

def main():      
    # PARTE 1 - CIFRAGEM E DECIFRAGEM  
    chave = input("Digite a chave: ")                                       # Solicita a chave ao usuário.    
    mensagem = input("Digite a mensagem: ")                                 # Solicita a mensagem ao usuário.    
                  
    cifra = Cifra_Decifra_Vigenere.Cifra_e_Decifra_de_Vigenere(chave)       # Cria o objeto da Cifra de Vigenère.
    mensagem_cifrada = cifra.cifragem(mensagem)                             # Realiza a cifragem da mensagem.    
    print("\nMensagem cifrada:", mensagem_cifrada)                          # Mostra a mensagem cifrada.

    mensagem_decifrada = cifra.decifragem(mensagem_cifrada)                 # Realiza a decifragem do criptograma.    
    print("Mensagem decifrada:", mensagem_decifrada)                        # Mostra a mensagem recuperada.

    # PARTE 2 - CRIPTOANÁLISE
    criptograma = input("\nDigite o criptograma para análise: ")
    
    idioma = input(
        "Digite o idioma do criptograma (portugues/ingles): "
    )

    # Cria o objeto de criptoanálise.
    analise = Criptoanalise_Vigenere.Criptoanalise_Vigenere()

    # Prepara o criptograma para a análise.
    texto = analise.preparar_texto(criptograma)

    # Estima possíveis tamanhos da chave.
    resultados = analise.estimar_tamanho_chave(texto, 20)

    print("\nÍndice de Coincidência:")

    for tamanho, ic in resultados:
        print(f"Tamanho {tamanho}: IC médio = {ic:.4f}")

    # Escolhe o tamanho mais provável.
    tamanho_chave = analise.escolher_tamanho_chave(resultados)

    print("\nTamanho da chave estimado:")
    print(tamanho_chave)

    # Recupera a chave.
    chave_recuperada = analise.recuperar_chave(
        texto,
        tamanho_chave,
        idioma
    )

    print("\nChave recuperada:")
    print(chave_recuperada)

    # Cria um objeto utilizando a chave recuperada.
    cifra_recuperada = (
        Cifra_Decifra_Vigenere.Cifra_e_Decifra_de_Vigenere(
            chave_recuperada
        )
    )

    # Decifra o criptograma usando a chave recuperada.
    mensagem_recuperada = cifra_recuperada.decifragem(criptograma)

    print("\nMensagem recuperada:")
    print(mensagem_recuperada)
if __name__ == "__main__":
    main()
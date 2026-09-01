import Cifra_Decifra_Vigenere
import Criptoanalise_Vigenere

def main():      
    # PARTE 1 - CIFRAGEM E DECIFRAGEM  
    chave = input("Digite a chave: ")                                       # Solicita a chave ao usuário.    
    mensagem = input("Digite a mensagem: ")                                 # Solicita a mensagem ao usuário.    
                  
    cifra = Cifra_Decifra_Vigenere.Cifra_e_Decifra_de_Vigenere(chave)       # Cria o objeto da Cifra de Vigenère.
    mensagem_cifrada = cifra.cifragem(mensagem)                             # Realiza a cifragem da mensagem.    
    print("\nMensagem cifrada:", mensagem_cifrada)                          # Mostra a mensagem cifrada.

    mensagem_decifrada = cifra.decifragem(mensagem_cifrada)                 # Realiza a decifragem do criptograma utilizando a mesma chave.    
    print("Mensagem decifrada:", mensagem_decifrada)                        # Mostra a mensagem recuperada.

    # PARTE 2 - CRIPTOANÁLISE
    criptograma = input("\nDigite o criptograma para análise: ")  
    idioma = input("Digite o idioma do criptograma (portugues/ingles): ")
    
    analise = Criptoanalise_Vigenere.Criptoanalise_Vigenere()               # Cria o objeto de criptoanálise.

    # Preparação de Criptograma
    texto = analise.preparar_texto(criptograma)                             # Prepara o criptograma para a análise.
    print("\n=== TEXTO PREPARADO PARA A CRIPTOANÁLISE ===") 
    print(texto)

    # Estimativa do tamanho da chave pelo IC
    resultados = analise.estimar_tamanho_chave(texto, 20)                   # Estima possíveis tamanhos da chave.
    analise.mostrar_candidatos_tamanho_chave(resultados)    

    # Escolha do tamanho provável da chave
    tamanho_chave = analise.escolher_tamanho_chave(resultados)
    if tamanho_chave is None: 
        print("\nNão foi possível estimar o tamanho da chave.") 
        return    
    print("\nTamanho da chave estimado:")
    print(tamanho_chave)

    # Análise estatística dos grupos
    resultados_grupos = analise.analizar_grupos(texto, tamanho_chave, idioma)

    # Reconstrução da chave candidata
    chave_recuperada = analise.recuperar_chave(resultados_grupos)
    print("\nChave recuperada:")
    print(chave_recuperada)

    # Decifragem do criptograma utilizando a chave recuperada
    cifra_recuperada = (Cifra_Decifra_Vigenere.Cifra_e_Decifra_de_Vigenere(chave_recuperada))

    # Decifra o criptograma usando a chave recuperada.
    mensagem_recuperada = cifra_recuperada.decifragem(criptograma)
    print("\nMensagem recuperada:")
    print(mensagem_recuperada)

if __name__ == "__main__":
    main()
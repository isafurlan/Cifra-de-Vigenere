from Cifra_Decifra_Vigenere import Cifra_e_Decifra_de_Vigenere
from Criptoanalise_Vigenere import Criptoanalise_Vigenere


def main():

    # Texto original que conhecemos.
    mensagem = (
        "A SEGURANCA COMPUTACIONAL E IMPORTANTE PARA PROTEGER "
        "INFORMACOES E SISTEMAS DIGITAIS"
    )

    # Chave que conhecemos apenas para realizar o teste.
    chave_original = "CASA"

    # Cria o objeto da cifra.
    cifra = Cifra_e_Decifra_de_Vigenere(chave_original)

    # Cifra a mensagem.
    criptograma = cifra.cifragem(mensagem)

    print("Mensagem original:")
    print(mensagem)

    print("\nChave original:")
    print(chave_original)

    print("\nCriptograma:")
    print(criptograma)

    # Cria o objeto de criptoanálise.
    analise = Criptoanalise_Vigenere()

    # Prepara o criptograma para a análise.
    texto = analise.preparar_texto(criptograma)

    print("\nTexto utilizado na análise:")
    print(texto)

    # Testa possíveis tamanhos de chave.
    resultados = analise.estimar_tamanho_chave(texto, 10)

    print("\nÍndice de Coincidência:")
    for tamanho, ic in resultados:
        print(f"Tamanho {tamanho}: IC médio = {ic:.4f}")

    # Por enquanto, vamos informar manualmente o tamanho
    # da chave para testar a recuperação da chave.
    tamanho_chave = analise.escolher_tamanho_chave(resultados)

    print("\nTamanho da chave estimado:")
    print(tamanho_chave)

    chave_recuperada = analise.recuperar_chave(
        texto,
        tamanho_chave,
        "portugues"
    )

    print("\nChave recuperada:")
    print(chave_recuperada)

     # Cria um objeto utilizando a chave recuperada.
    cifra_recuperada = Cifra_e_Decifra_de_Vigenere(chave_recuperada)

    # Utiliza a chave recuperada para decifrar o criptograma.
    mensagem_recuperada = cifra_recuperada.decifragem(criptograma)

    print("\nMensagem recuperada:")
    print(mensagem_recuperada)

if __name__ == "__main__":
    main()
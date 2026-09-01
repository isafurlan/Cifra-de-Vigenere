"""
Cifra e decifra texto com Vigenère.
Alfabeto adotado: A-Z, com 26 letras.
Regras:
    - Letras minúsculas são convertidas para maiúsculas.
    - Somente letras A-Z são cifradas/decifradas.
    - Espaços, números, pontuação, acentos e outros caracteres
      são preservados.
    - Caracteres fora de A-Z não avançam a chave.
    - A chave deve conter somente letras A-Z.
"""

class Cifra_e_Decifra_de_Vigenere():
    def __init__(self, chave):
        self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'    # Define o alfabeto utilizado pela cifra, 26 letras de A até Z.

        # Validação da chave
        if not chave:
            raise ValueError("A chave não pode ser vazia.")
        if any(letra.upper() not in self.alphabet for letra in chave): 
            raise ValueError("A chave deve conter apenas letras de A-Z.")     

        self.key = chave.upper()                        # Converte a chave para letras maiúsculas.        
        
        self.letter_to_index = dict(zip(self.alphabet, range(len(self.alphabet))))  # Cria um dicionário que relaciona cada letra ao seu valor numérico.
        self.index_to_letter = dict(zip(range(len(self.alphabet)), self.alphabet))  # Cria o dicionário inverso que relaciona valor numérico a uma letra.

    """
        Implementação da cifragem de Vigenère.
        Cifra uma mensagem utilizando a fórmula:
            C = (P + K) mod 26
        onde:
        P = valor numérico da letra do texto claro
        K = valor numérico da letra da chave
        C = valor numérico da letra cifrada
    """

    def cifragem(self, mensagem):
        mensagem = mensagem.upper()                      # Converte a mensagem para letras maiúsculas.     
        mensagem_cifrada = ''                            # Variável que armazenará o resultado da cifragem.
        j = 0                                            # Índice utilizado para percorrer a chave.           
      
        for letter in mensagem:                          # Percorre cada caractere da mensagem.
            if letter not in self.alphabet:              # Verifica se o caractere pertence ao alfabeto adotado (A-Z). 
                mensagem_cifrada += letter               # Preserva espaços, números, acentos, pontuação e caracteres especiais.             
                continue                                 # Esses caracteres também NÃO avançam a chave.

            valor_mensagem = self.letter_to_index[letter]                                     # Obtém o valor numérico da letra da mensagem.
            valor_chave = self.letter_to_index[self.key[j]]                                   # Obtém o valor numérico da letra correspondente da chave.
            valor_cifrado = (valor_mensagem + valor_chave) % len(self.alphabet)               # Aplica a fórmula matemática da Cifra de Vigenère: C = (P + K) mod 26
            mensagem_cifrada += self.index_to_letter[valor_cifrado]                           # Converte o valor numérico novamente para uma letra.

            j = (j + 1) % len(self.key)                   # Avança para a próxima posição da chave. Quando chega ao final da chave, retorna para a primeira posição. 
                
        return mensagem_cifrada                           # Retorna a mensagem cifrada.  
    
    """
        Implementação da decifragem de Vigenère.
        Decifra uma mensagem utilizando a fórmula:
            P = (C - K) mod 26
        onde:
        P = valor numérico da letra original
        C = valor numérico da letra do criptograma 
        K = valor numérico da letra da chave
    """

    def decifragem(self, criptograma):
        # Validação do criptograma
        if criptograma is None:
            raise ValueError("O criptograma não pode ser nulo.")

        criptograma = criptograma.upper()                 # Converte o criptograma para letras maiúsculas.
        mensagem_decifrada = ''                           # Variável que armazenará o texto decifrado.
        j = 0                                             # Índice utilizado para percorrer a chave.  

        for letter in criptograma:                        # Percorre cada caractere do criptograma.             
            if letter not in self.alphabet:               # Verifica se o caractere pertence ao alfabeto adotado (A-Z). 
                mensagem_decifrada += letter              # Preserva espaços, números, acentos, pontuação e caracteres especiais.
                continue                                  # Esses caracteres também NÃO avançam a chave.
                
            valor_criptograma = self.letter_to_index[letter]                                 # Obtém o valor numérico da letra do criptograma.
            valor_chave = self.letter_to_index[self.key[j]]                                  # Obtém o valor numérico da letra correspondente da chave.
            valor_original = (valor_criptograma - valor_chave) % len(self.alphabet)          # Aplica a fórmula matemática da decifragem de Vigenère: P = (C - K) mod 26
            mensagem_decifrada += self.index_to_letter[valor_original]                       # Converte o valor numérico novamente para uma letra.
                 
            j = (j + 1) % len(self.key)                   # Avança para a próxima posição da chave. Quando chega ao final da chave, retorna para a primeira posição. 

        return mensagem_decifrada                         # Retorna o texto original recuperado.
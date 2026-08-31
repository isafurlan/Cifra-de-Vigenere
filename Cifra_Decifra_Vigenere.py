"""Cifra e decifra texto com Vigenère.
O alfabeto adotado é o latino com 26 caracteres de A-Z.
Letras minúsculas são convertidas para maiúsculas.
Caracteres que não pertencem ao alfabeto A-Z, como símbolos
de pontuação, são desconsiderados ou convertidos para letras sem acento.
Esse funcionamento é válido tanto para a chave quanto para a mensagem.
Exceção: números na chave serão convertidos para letras, mas na mensagem serão preservados.
A chave deve conter pelo menos um caractere válido.
"""

import unicodedata

class Cifra_e_Decifra_de_Vigenere():
    def __init__(self, chave):
        self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'    # Define o alfabeto utilizado pela cifra, 26 letras de A até Z.
        self.key = chave.upper()                        # Converte a chave para letras maiúsculas.

        self.letter_to_index = dict(zip(self.alphabet, range(len(self.alphabet))))  # Cria um dicionário que relaciona cada letra ao seu valor numérico.
        self.index_to_letter = dict(zip(range(len(self.alphabet)), self.alphabet))  # Cria o dicionário inverso que relaciona valor numérico a uma letra.

        chave_limpa = self.remover_acentos(self.key)
        chave_processada = []
        for c in chave_limpa:
            if c.isdigit():
                chave_processada.append(self.index_to_letter[int(c)])  # Converte números para letras correspondentes no alfabeto.
            if c in self.alphabet:
                chave_processada.append(c) 
                                
        self.key = ''.join(chave_processada)

        if not self.key:      # Verifica se a chave é válida.
            raise ValueError("A chave deve conter apenas letras ou números válidos.")

    @staticmethod
    def remover_acentos(texto):
        texto_nfd = unicodedata.normalize('NFD', texto)  # Normaliza o texto para decompor caracteres acentuados.
        return ''.join(c for c in texto_nfd if unicodedata.category(c) != 'Mn')

    
    def cifragem(self, message):
        message = self.remover_acentos(message.upper())        # Converte a mensagem para letras maiúsculas.     
        mesage_cifrada = ''                                    # Variável que armazenará o resultado da cifragem.
        j = 0                                                  # Índice utilizado para percorrer a chave.           
      
        for letter in message:                                 # Percorre cada caractere da mensagem.
            if letter not in self.alphabet:                    # Verifica se o caractere pertence ao alfabeto adotado (A-Z). 
                mesage_cifrada += letter                       # Preserva espaços, acentos, pontuação e caracteres especiais.             
                continue                                       # Esses caracteres também NÃO avançam a chave.

            number = (self.letter_to_index[letter] + self.letter_to_index[self.key[j]]) % len(self.alphabet)  # Aplica a fórmula matemática da Cifra de Vigenère: C = (P + K) mod 26
            mesage_cifrada += self.index_to_letter[number]     # Converte o valor numérico novamente para uma letra.
            j = (j+1) % len(self.key)                          # Avança para a próxima posição da chave. Quando chega ao final da chave, retorna para a primeira posição. 

        return mesage_cifrada

    def decifragem(self, criptograma):
        criptograma = self.remover_acentos(criptograma.upper())
        mensagem_decifrada = ''                           
        j = 0      # Índice utilizado para percorrer a chave.  

        for letter in criptograma:                        # Percorre cada caractere do criptograma.             
            if letter not in self.alphabet:               # Verifica se o caractere pertence ao alfabeto adotado (A-Z). 
                mensagem_decifrada += letter              # Preserva espaços, números, acentos, pontuação e caracteres especiais.
                continue                                  # Esses caracteres também NÃO avançam a chave.
                
            number = (self.letter_to_index[letter] - self.letter_to_index[self.key[j]]) % len(self.alphabet)  # Aplica a fórmula matemática da Cifra de Vigenère: P = (C - K) mod 26
            mensagem_decifrada += self.index_to_letter[number]      # Converte o valor numérico novamente para uma letra.
            j = (j+1) % len(self.key)                               # Avança para a próxima posição da chave. Quando chega ao final da chave, retorna para a primeira posição.
        return mensagem_decifrada      # Retorna o texto original recuperado.
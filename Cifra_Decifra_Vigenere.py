"""Cifra e decifra texto com Vigenère.
O alfabeto adotado é A-Z.
Letras minúsculas são convertidas para maiúsculas.
Caracteres que não pertencem ao alfabeto A-Z são preservados
e não avançam a chave."""

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

    def cifragem(self, message):
        message = message.upper()                        # Converte a mensagem para letras maiúsculas.     
        mesage_cifrada = ''                              # Variável que armazenará o resultado da cifragem.
        j = 0                                            # Índice utilizado para percorrer a chave.           
      
        for letter in message:                           # Percorre cada caractere da mensagem.
            if letter not in self.alphabet:              # Verifica se o caractere pertence ao alfabeto adotado (A-Z). 
                mesage_cifrada += letter                 # Preserva espaços espaços, números, acentos, pontuação e caracteres especiais.             
                continue                                 # Esses caracteres também NÃO avançam a chave.

            valor_mensagem = self.letter_to_index[letter]                              # Obtém o valor numérico da letra da mensagem.
            valor_chave = self.letter_to_index[self.key[j]]                            # Obtém o valor numérico da letra correspondente da chave.
            number = (valor_mensagem + valor_chave) % len(self.alphabet)               # Aplica a fórmula matemática da Cifra de Vigenère: C = (P + K) mod 26
            mesage_cifrada += self.index_to_letter[number]                             # Converte o valor numérico novamente para uma letra.

            if j == len(self.key) - 1:                    # Avança para a próxima posição da chave. Quando chega ao final da chave, retorna para a primeira posição. 
                j = 0
            else:
                j += 1

        return mesage_cifrada                             # Retorna a mensagem cifrada.  

    def decifragem(self, criptograma):
        criptograma = criptograma.upper()                 # Converte o criptograma para letras maiúsculas.
        mensagem_decifrada = ''                           # Variável que armazenará o texto decifrado.
        j = 0                                             # Índice utilizado para percorrer a chave.  

        for letter in criptograma:                        # Percorre cada caractere do criptograma.             
            if letter not in self.alphabet:               # Verifica se o caractere pertence ao alfabeto adotado (A-Z). 
                mensagem_decifrada += letter              # Preserva espaços, números, acentos, pontuação e caracteres especiais.
                continue                                  # Esses caracteres também NÃO avançam a chave.
                
            valor_criptograma = self.letter_to_index[letter]                           # Obtém o valor numérico da letra do criptograma.
            valor_chave = self.letter_to_index[self.key[j]]                            # Obtém o valor numérico da letra correspondente da chave.
            number_original = (valor_criptograma - valor_chave) % len(self.alphabet)   # Aplica a fórmula matemática da decifragem de Vigenère: P = (C - K) mod 26
            mensagem_decifrada += self.index_to_letter[number_original]                         # Converte o valor numérico novamente para uma letra.
                 
            j = (j + 1) % len(self.key)                   # Avança para a próxima posição da chave. Quando chega ao final da chave, retorna para a primeira posição. 

        return mensagem_decifrada                     # Retorna o texto original recuperado.
import unicodedata

class Cifra_de_Vigenere():
    def __init__(self, chave):
        self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.key = self.remover_acentos(chave.upper())
        self.letter_to_index = dict(zip(self.alphabet, range(len(self.alphabet))))
        self.index_to_letter = dict(zip(range(len(self.alphabet)), self.alphabet))

    @staticmethod
    def remover_acentos(texto):
        #Normaliza o texto de composição de caracteres Unicode, removendo acentos e diacríticos.
        texto_nfd = unicodedata.normalize('NFD', texto)
        texto_sem_acento = ''.join(c for c in texto_nfd if unicodedata.category(c) != 'Mn')
        return texto_sem_acento

    def cifragem(self, message):
        message = self.remover_acentos(message.upper())
        #message = message.split()
        mesage_cifrada = ''
        j = 0
        

        '''for n in range(len(message)):
            word = message[n]'''

        seg_message = [message[i: i + len(self.key)] for i in range(0, len(message), len(self.key))]

        '''for i in range(0, len(message), len(self.key)): # cortar do tamanho da chave
            seg_message.append(message[i:i + len(self.key)])'''

        for word in seg_message:
            for letter in word:
                if letter not in self.alphabet:
                    mesage_cifrada += letter
                    continue
                number = (self.letter_to_index[letter] + self.letter_to_index[self.key[j]]) % len(self.alphabet)
                mesage_cifrada += self.index_to_letter[number]

                if j == len(self.key) - 1:
                    j = 0
                else:
                    j += 1

        return mesage_cifrada

    def decifragem(self, mesage_cifrada):
        mesage_cifrada = mesage_cifrada.upper()
        mensagem_original = ''
        j = 0

        for letter in mesage_cifrada:
            if letter not in self.alphabet:
                mensagem_original += letter
                continue
            #Lógica matemática inversa da cifragem, subtraindo o índice da letra da chave do índice da letra cifrada.
            number = (self.letter_to_index[letter] - self.letter_to_index[self.key[j]]) % len(self.alphabet)
            mensagem_original += self.index_to_letter[number]

            j = (j + 1) % len(self.key)

        return mensagem_original

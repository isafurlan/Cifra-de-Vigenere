class Cifra_de_Vigenere():
    def __init__(self, chave):
        self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.key = chave.upper()

        self.letter_to_index = dict(zip(self.alphabet, range(len(self.alphabet))))
        self.index_to_letter = dict(zip(range(len(self.alphabet)), self.alphabet))

    def cifragem(self, message):
        message = message.upper()
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


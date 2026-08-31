class Criptoanalise_Vigenere():

    def __init__(self):        
        self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'    # Define o alfabeto utilizado na análise, 26 letras de A até Z.
       
        self.letter_to_index = dict(zip(self.alphabet, range(len(self.alphabet))))    # Relaciona cada letra ao seu valor numérico.        
        self.index_to_letter = dict(zip(range(len(self.alphabet)), self.alphabet))    # Relaciona cada valor numérico à sua letra.

        # Frequência aproximada das letras em textos em português.
        self.frequencia_portugues = {
                            'A': 14.63, 'B': 1.04, 'C': 3.88, 'D': 4.99,
                            'E': 12.57, 'F': 1.02, 'G': 1.30, 'H': 1.28,
                            'I': 6.18, 'J': 0.40, 'K': 0.02, 'L': 2.78,
                            'M': 4.74, 'N': 5.05, 'O': 10.73, 'P': 2.52,
                            'Q': 1.20, 'R': 6.53, 'S': 7.81, 'T': 4.34,
                            'U': 4.63, 'V': 1.67, 'W': 0.01, 'X': 0.21,
                            'Y': 0.01, 'Z': 0.47
                        }    

        # Frequência aproximada das letras em textos em inglês.
        self.frequencia_ingles = {
                            'A': 8.17, 'B': 1.49, 'C': 2.78, 'D': 4.25,
                            'E': 12.70, 'F': 2.23, 'G': 2.02, 'H': 6.09,
                            'I': 6.97, 'J': 0.15, 'K': 0.77, 'L': 4.03,
                            'M': 2.41, 'N': 6.75, 'O': 7.51, 'P': 1.93,
                            'Q': 0.10, 'R': 5.99, 'S': 6.33, 'T': 9.06,
                            'U': 2.76, 'V': 0.98, 'W': 2.36, 'X': 0.15,
                            'Y': 1.97, 'Z': 0.07
                        }            

    def preparar_texto(self, texto):
        texto = texto.upper()                           # Converte o criptograma para letras maiúsculas.
        texto_limpo = ''                                # Variável que armazenará somente as letras A-Z.

        for letra in texto:                             # Percorre cada caractere do criptograma.
            if letra in self.alphabet:                  # Verifica se o caractere pertence ao alfabeto A-Z.
                texto_limpo += letra

        return texto_limpo

    # Contagem da frequência das letras
    def frequencia_letras(self, texto):           
        frequencias = {}                                # Cria um dicionário para armazenar a quantidade de ocorrências de cada letra do alfabeto.
        
        for letra in self.alphabet:                     # Inicializa todas as letras com frequência zero.
            frequencias[letra] = 0
        
        for letra in texto:                             # Percorre cada letra do texto.           
            if letra in frequencias:                     
                frequencias[letra] += 1                 # Incrementa a quantidade de ocorrências da letra.

        return frequencias

    # Calculo do Índice de Coincidência
    def indice_coincidencia(self, texto):       
        N = len(texto)                                  # Obtém a quantidade total de letras do texto.   
        
        if N <= 1:                                      # Não é possível calcular o índice com menos de duas letras.
            return 0
        
        frequencias = self.frequencia_letras(texto)     # Obtém a frequência de cada letra.       
        soma = 0                                        # Variável que armazenará a soma da fórmula.
        
        for letra in self.alphabet:                     # Percorre todas as letras do alfabeto.           
            f = frequencias[letra]                      # Obtém a frequência da letra.            
            soma += f * (f - 1)                         # Calcula f * (f - 1).
        
        ic = soma / (N * (N - 1))                       # Aplica a fórmula do Índice de Coincidência.

        return ic

    # Estimativa do tamanho da chave usando o Índice de Coincidência (IC).
    # Separa os grupos.
    def separar_grupos(self, texto, tamanho_chave):        
        grupos = []                                     # Cria uma lista vazia para armazenar os grupos.  
       
        for i in range(tamanho_chave):                  # Cria um grupo para cada posição da chave.
            grupos.append('')
       
        for i, letra in enumerate(texto):               # Percorre todas as letras do texto.            
            posicao = i % tamanho_chave                 # Calcula a posição do grupo ao qual a letra pertence.            
            grupos[posicao] += letra                    # Adiciona a letra ao grupo correspondente.

        return grupos
    
    def estimar_tamanho_chave(self, texto, tamanho_maximo=20):
        resultados = []
        
        for tamanho in range(1, tamanho_maximo + 1):            # Testa possíveis tamanhos para a chave.            
            grupos = self.separar_grupos(texto, tamanho)        # Divide o texto em grupos de acordo com o tamanho testado.
            indices = []                                        # Armazena os índices de coincidência dos grupos.
            
            for grupo in grupos:                                # Calcula o IC de cada grupo.
                if len(grupo) > 1:                              # Só utiliza grupos com quantidade suficiente de letras.
                    ic = self.indice_coincidencia(grupo)
                    indices.append(ic)
            
            if len(indices) == 0:                               # Se não houver grupos suficientes, ignora o tamanho.
                continue
            
            media_ic = sum(indices) / len(indices)              # Calcula o IC médio dos grupos.

            resultados.append((tamanho, media_ic))              # Guarda o tamanho e o IC correspondente.

        resultados.sort(key=lambda x: x[1], reverse=True)       # Ordena os resultados pelo IC médio, do maior para o menor.

        return resultados    

    def escolher_tamanho_chave(self, resultados):
        if len(resultados) == 0:
            return None

        # O resultado com maior IC é o principal candidato.
        maior_ic = resultados[0][1]

        # Define um limite para considerar um IC como próximo
        # do melhor resultado.
        limite = maior_ic * 0.75

        # Ordena os tamanhos em ordem crescente.
        resultados_ordenados = sorted(resultados)

        for tamanho, ic in resultados_ordenados:

            # Ignora resultados com IC muito abaixo do melhor.
            if ic < limite:
                continue

            # Verifica se o tamanho é divisor de algum candidato maior.
            for tamanho_maior, ic_maior in resultados_ordenados:

                if tamanho_maior > tamanho:

                    if tamanho_maior % tamanho == 0:

                        # Se o tamanho menor também apresenta
                        # um IC alto, ele pode representar
                        # o período fundamental da chave.
                        if ic >= limite:
                            return tamanho

        # Caso nenhum divisor adequado seja encontrado,
        # retorna o tamanho com maior IC.
        return resultados[0][0]
    
    # Calcula a frequência percentual.
    def frequencia_percentual(self, texto):
        frequencias = self.frequencia_letras(texto)

        total = len(texto)

        percentuais = {}

        if total == 0:
            return percentuais

        for letra in self.alphabet:
            percentuais[letra] = (frequencias[letra] / total) * 100

        return percentuais

    # Testar um deslocamento.
    def deslocar_grupo(self, grupo, deslocamento):
        resultado = ''

        for letra in grupo:
            valor = self.letter_to_index[letra]
            novo_valor = (valor - deslocamento) % len(self.alphabet)
            resultado += self.index_to_letter[novo_valor]

        return resultado

    def qui_quadrado(self, texto, frequencia_esperada):

        # Obtém a quantidade de letras do texto.
        total = len(texto)

        # Se o texto estiver vazio, não é possível realizar a análise.
        if total == 0:
            return float('inf')

        # Obtém a frequência observada de cada letra.
        frequencias = self.frequencia_letras(texto)

        # Inicializa o valor do qui-quadrado.
        chi = 0

        # Percorre todas as letras do alfabeto.
        for letra in self.alphabet:

            # Quantidade observada da letra.
            observada = frequencias[letra]

            # Quantidade esperada da letra.
            esperada = (frequencia_esperada[letra] / 100) * total

            # Evita divisão por zero.
            if esperada > 0:
                chi += ((observada - esperada) ** 2) / esperada

        return chi

    def encontrar_melhor_deslocamento(self, grupo, frequencia_esperada):

        melhor_deslocamento = 0
        menor_chi = float('inf')

        # Testa todos os 26 deslocamentos possíveis.
        for deslocamento in range(len(self.alphabet)):

            # Decifra o grupo usando o deslocamento testado.
            grupo_decifrado = self.deslocar_grupo(
                grupo,
                deslocamento
            )

            # Calcula o qui-quadrado desse deslocamento.
            chi = self.qui_quadrado(
                grupo_decifrado,
                frequencia_esperada
            )

            # Verifica se esse deslocamento é melhor
            # que o melhor encontrado até agora.
            if chi < menor_chi:
                menor_chi = chi
                melhor_deslocamento = deslocamento

        return melhor_deslocamento, menor_chi

    def recuperar_chave(self, texto, tamanho_chave, idioma='portugues'):

        # Seleciona a distribuição de frequência correspondente ao idioma.
        if idioma == 'ingles':
            frequencia_esperada = self.frequencia_ingles
        else:
            frequencia_esperada = self.frequencia_portugues

        # Divide o criptograma de acordo com o tamanho da chave.
        grupos = self.separar_grupos(texto, tamanho_chave)

        chave = ''

        # Analisa cada grupo.
        for grupo in grupos:

            # Descobre o melhor deslocamento para o grupo.
            deslocamento, chi = self.encontrar_melhor_deslocamento(
                grupo,
                frequencia_esperada
            )

            # Converte o deslocamento para a letra correspondente.
            letra = self.index_to_letter[deslocamento]

            # Adiciona a letra à chave.
            chave += letra

        return chave
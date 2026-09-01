"""
CRIPTOANÁLISE DA CIFRA DE VIGENÈRE

Metodologia utilizada:
    1. Limpeza do criptograma, considerando somente A-Z;
    2. Estimativa do tamanho da chave pelo Índice de Coincidência;
    3. Separação do criptograma em grupos conforme as posições da chave;
    4. Análise estatística de cada grupo;
    5. Teste dos 26 possíveis deslocamentos;
    6. Seleção do deslocamento com menor qui-quadrado;
    7. Reconstrução da chave candidata.

O Índice de Coincidência é utilizado para estimar o período da chave.
O teste de qui-quadrado é utilizado para identificar o deslocamento
mais compatível com a distribuição de frequência do idioma analisado.

Alfabeto adotado: A-Z.
"""

class Criptoanalise_Vigenere():

    def __init__(self):        
        self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'    # Define o alfabeto utilizado na análise, 26 letras de A até Z.
       
        self.letter_to_index = dict(zip(self.alphabet, range(len(self.alphabet))))    # Relaciona cada letra ao seu valor numérico.        
        self.index_to_letter = dict(zip(range(len(self.alphabet)), self.alphabet))    # Relaciona cada valor numérico à sua letra.

        # Frequência aproximada das letras em textos em português.
        # Os valores estão em porcentagem e serão utilizados como distribuição esperada no teste de qui-quadrado.
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
        # Os valores estão em porcentagem e serão utilizados como distribuição esperada no teste de qui-quadrado.
        self.frequencia_ingles = {
                            'A': 8.17, 'B': 1.49, 'C': 2.78, 'D': 4.25,
                            'E': 12.70, 'F': 2.23, 'G': 2.02, 'H': 6.09,
                            'I': 6.97, 'J': 0.15, 'K': 0.77, 'L': 4.03,
                            'M': 2.41, 'N': 6.75, 'O': 7.51, 'P': 1.93,
                            'Q': 0.10, 'R': 5.99, 'S': 6.33, 'T': 9.06,
                            'U': 2.76, 'V': 0.98, 'W': 2.36, 'X': 0.15,
                            'Y': 1.97, 'Z': 0.07
                        }            

    """
    Preparando o criptograma para a análise estatística.
    Somente letras A-Z são mantidas, pois as frequências utilizadas 
    na criptoanálise correspondem ao alfabeto adotado.
    Espaços, números, pontuação, acentos e outros caracteres
    não participam dos cálculos estatísticos.
    """
    # Preparar criptograma
    def preparar_texto(self, texto):
        if texto is None:
            raise ValueError("O texto não pode ser nulo.")
        
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

    """
    Calculando o Índice de Coincidência (IC) utilizando a fórmula:
            IC = Σ f_i(f_i - 1) / N(N - 1)
    onde:
    f_i = frequência absoluta da letra i
    N   = quantidade total de letras
    
    O IC auxilia na identificação do período da chave.
    Quando o texto é dividido de acordo com o tamanho correto
    da chave, cada grupo tende a apresentar características
    estatísticas semelhantes às de um texto natural.
    """
    # Calculo do Índice de Coincidência (ic)
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

    """
    Divide o criptograma em grupos correspondentes às posições da chave.
    Para uma chave de tamanho 3:
        Grupo 0 -> posições 0, 3, 6, 9, ...
        Grupo 1 -> posições 1, 4, 7, 10, ...
        Grupo 2 -> posições 2, 5, 8, 11, ...

    Cada grupo é tratado como uma cifra de César, pois todas as suas letras 
    foram cifradas utilizando a mesma posição da chave.
    """        
    # Separa os grupos.
    def separar_grupos(self, texto, tamanho_chave):       
        if tamanho_chave <= 0:
            raise ValueError("O tamanho da chave deve ser maior que zero.") 

        grupos = []                                     # Cria uma lista vazia para armazenar os grupos.  
       
        for i in range(tamanho_chave):                  # Cria um grupo para cada posição da chave.
            grupos.append('')
       
        for i, letra in enumerate(texto):               # Percorre todas as letras do texto.            
            posicao = i % tamanho_chave                 # Calcula a posição do grupo ao qual a letra pertence.            
            grupos[posicao] += letra                    # Adiciona a letra ao grupo correspondente.

        return grupos

    """
    Testando possíveis tamanhos de chave utilizando o Índice de Coincidência.
    Para cada tamanho candidato:
        1. O criptograma é dividido em grupos;
        2. O IC de cada grupo é calculado;
        3. É calculado o IC médio dos grupos.

    Os resultados são ordenados pelo IC médio.
    Valores elevados indicam candidatos relevantes para o período da chave.
    """
    # Estimar tamnho de chave
    def estimar_tamanho_chave(self, texto, tamanho_maximo=20):
        if tamanho_maximo <= 0:
            raise ValueError("O tamanho máximo da chave deve ser maior que zero.")

        resultados = []
        
        for tamanho in range(1, tamanho_maximo + 1):            # Testa possíveis tamanhos para a chave.            
            grupos = self.separar_grupos(texto, tamanho)        # Divide o texto em grupos de acordo com o tamanho testado.
            indices = []                                        # Armazena os índices de coincidência dos grupos.
            
            for grupo in grupos:                                # Calcula o IC de cada grupo.
                if len(grupo) > 1:                              # Só utiliza grupos com quantidade suficiente de letras.
                    ic = self.indice_coincidencia(grupo)
                    indices.append(ic)          

            if not indices:                                     # Se não houver grupos suficientes, ignora o tamanho.
                continue
            
            media_ic = sum(indices) / len(indices)              # Calcula o IC médio dos grupos.

            resultados.append((tamanho, media_ic))              # Guarda o tamanho e o IC correspondente.

        resultados.sort(key=lambda x: x[1], reverse=True)       # Ordena os resultados pelo IC médio, do maior para o menor.

        return resultados   

    """
    Selecionando um candidato para o tamanho da chave.
    O maior IC não é automaticamente considerado como o período fundamental,
    pois múltiplos do tamanho real da chave também podem apresentar IC elevado.
    Portanto, quando existem candidatos fortes relacionados por múltiplos, o 
    menor período é priorizado.
    Caso não exista uma relação clara entre os candidatos, utiliza-se aquele que 
    apresentou o maior IC.
    """
    # Escolher tamanho da chave
    def escolher_tamanho_chave(self, resultados):
        if len(resultados) == 0:
            return None
        
        maior_ic = max(ic for tamanho, ic in resultados)         # Maior IC encontrado.    

        # Seleciona candidatos próximos do melhor IC. Essa margem permite considerar 
        # a variação natural dos valores de IC entre os diferentes tamanhos.        
        candidatos_fortes = [
            (tamanho, ic)
            for tamanho, ic in resultados
            if ic >= maior_ic * 0.80
        ]

        candidatos_fortes.sort(key=lambda x: x[0])                # Ordena os candidatos pelo tamanho.

        # Procura um candidato menor que seja divisor de outro candidato forte.
        for tamanho, ic in candidatos_fortes:
            for tamanho_maior, ic_maior in candidatos_fortes:
                if tamanho_maior > tamanho:
                    if tamanho_maior % tamanho == 0:
                        return tamanho

        # Caso não seja identificada uma relação de múltiplos, escolhe o candidato que apresentou maior IC.
        melhor = max(resultados,key=lambda x: x[1])

        return melhor[0]

    """
    Converte as frequências absolutas das letras
    em frequências percentuais.
    """
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

    """
    Aplica um deslocamento de César ao grupo.
    Como estamos tentando recuperar o texto original, utilizando 
    a operação:
        P = (C - K) mod 26
    onde:
    C = letra do criptograma
    K = deslocamento candidato
    P = letra recuperada
    """
    # Aplicando um deslocamento.
    def deslocar_grupo(self, grupo, deslocamento):
        resultado = ''

        for letra in grupo:
            valor = self.letter_to_index[letra]                             # Converte a letra para seu valor numérico.
            novo_valor = (valor - deslocamento) % len(self.alphabet)        # Aplica a subtração modular.
            resultado += self.index_to_letter[novo_valor]                   # Converte o resultado para uma letra.

        return resultado

    """
    Calcula o teste de qui-quadrado para comparar a distribuição observada 
    com a distribuição esperada, utilizando a fórmula:
        χ² = Σ (O - E)² / E
    onde:
    O = frequência observada
    E = frequência esperada
    Quanto menor o valor de χ², menor é a diferença entre as duas distribuições.
    Assim, o menor χ² indica o deslocamento que produz uma distribuição mais 
    compatível com o idioma analisado.
    """
    #Calculando o qui_quadrado
    def qui_quadrado(self, texto, frequencia_esperada):        
        total = len(texto)                                            # Obtém a quantidade de letras do texto.      

        # Se o texto estiver vazio, não é possível realizar a análise.
        if total == 0:
            return float('inf')
        
        frequencias = self.frequencia_letras(texto)                   # Obtém a frequência observada de cada letra.  
        
        chi = 0                                                       # Inicializa o valor do qui-quadrado.

        # Calcula o termo do qui-quadrado para cada letra.
        for letra in self.alphabet:                                   # Percorre todas as letras do alfabeto.
            observada = frequencias[letra]                            # Frequência observada da letra.            
            esperada = (frequencia_esperada[letra] / 100) * total     # Frequência esperada segundo o idioma.
            
            if esperada > 0:                                          # Evita divisão por zero.
                chi += ((observada - esperada) ** 2) / esperada

        return chi

    """
    Testa os 26 possíveis deslocamentos de um grupo.
    Cada deslocamento representa uma possível letra da chave:
        0 -> A
        1 -> B
        ...
        25 -> Z
    Para cada possibilidade:
        1. O grupo é decifrado;
        2. A distribuição das letras é calculada;
        3. O qui-quadrado é calculado.
    O deslocamento com menor qui-quadrado é escolhido.
    """
    #Calculando o melhor deslocamento
    def encontrar_melhor_deslocamento(self, grupo, frequencia_esperada):

        melhor_deslocamento = 0
        menor_chi = float('inf')

        # Testa todos os 26 deslocamentos possíveis.
        for deslocamento in range(len(self.alphabet)):            
            grupo_decifrado = self.deslocar_grupo(grupo,deslocamento)           # Decifra o grupo usando o deslocamento testado.            
            chi = self.qui_quadrado(grupo_decifrado,frequencia_esperada)        # Calcula o qui-quadrado desse deslocamento. 
                       
            if chi < menor_chi:                                                 # Verifica esse deslocamento, e no caso atualiza o melhor candidato. 
                menor_chi = chi
                melhor_deslocamento = deslocamento

        return melhor_deslocamento, menor_chi

    """
    Realiza e apresenta a análise estatística de cada grupo.
    Para cada posição da chave:
        - testa os 26 deslocamentos possíveis;
        - calcula o qui-quadrado;
        - seleciona o deslocamento com menor valor;
        - converte o deslocamento para a letra correspondente.
    Retorna os resultados da análise para cada grupo.
    """
    # Analizando grupos
    def analizar_grupos(self, texto, tamanho_chave, idioma='portugues'):
        if tamanho_chave <= 0:
            raise ValueError("O tamanho da chave deve ser maior que zero.")

        # Seleciona a distribuição de frequência correspondente ao idioma.
        if idioma.lower() == 'ingles':
            frequencia_esperada = self.frequencia_ingles
        elif idioma.lower() == 'portugues':
            frequencia_esperada = self.frequencia_portugues
        else:
            raise ValueError("O idioma deve ser 'portugues' ou 'ingles'.")
        
        grupos = self.separar_grupos(texto, tamanho_chave)                      # Divide o criptograma de acordo com o tamanho da chave.

        resultados = []
        print("\n=== ANÁLISE DOS GRUPOS ===")

        # Analisa cada posição da chave.
        for i, grupo in enumerate(grupos):
            deslocamento, chi = (self.encontrar_melhor_deslocamento(grupo,frequencia_esperada))
         
            letra = self.index_to_letter[deslocamento]                          # Converte o deslocamento para a letra da chave.

            resultados.append((i + 1,deslocamento,letra,chi))

            print(
                f"Grupo {i + 1}: "
                f"deslocamento = {deslocamento:2d}, "
                f"letra = {letra}, "
                f"qui-quadrado = {chi:.4f}"
            )

        return resultados
    
    """
    Exibe os principais candidatos encontrados durante a estimativa do tamanho da chave.
    A apresentação desses resultados permite demonstrar as hipóteses testadas antes da
    escolha do tamanho final.
    """
    #Aprsentando resultados
    def mostrar_candidatos_tamanho_chave(self,resultados,quantidade=10):
        print("\n=== CANDIDATOS AO TAMANHO DA CHAVE ===")
        print(f"{'Tamanho':<12}{'IC médio':<15}")

        # Mostra somente os melhores candidatos.
        for tamanho, ic in resultados[:quantidade]:
            print(f"{tamanho:<12}{ic:.6f}")

    """
    Reconstrói uma chave candidata a partir dos resultados da análise estatística dos grupos.
    """

    def recuperar_chave(self, resultados):
        chave = ''

        for resultado in resultados:
            letra = resultado[2]
            chave += letra

        return chave
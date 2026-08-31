# 🔐 Cifra de Vigenère

Implementação própria da Cifra de Vigenère em Python — cifração, decifração e um ataque de criptoanálise para recuperação de chave, sem uso de bibliotecas prontas de criptografia.

Projeto desenvolvido como **Trabalho 1** da disciplina **CIC0201 - Segurança Computacional**, da Universidade de Brasília (UnB).

## ✨ Funcionalidades

- **Cifração**: recebe uma chave e uma mensagem em texto claro e produz o criptograma correspondente.
- **Decifração**: recebe a mesma chave e o criptograma e recupera a mensagem original.
- **Validação de chave**: chaves vazias ou que contenham qualquer caractere fora do alfabeto A-Z são rejeitadas com uma mensagem de erro.
- **Criptoanálise (ataque à cifra)**: a partir de um criptograma com chave desconhecida, estima o tamanho provável da chave, analisa a frequência de letras de cada subgrupo e reconstrói a chave, decifrando a mensagem original.

## 🔤 Como o alfabeto é tratado

O alfabeto adotado é o latino de 26 letras (A-Z). As regras de processamento são:

| Tipo de caractere | Na chave | Na mensagem |
|---|---|---|
| Letras minúsculas | Convertidas para maiúsculas | Convertidas para maiúsculas |
| Letras acentuadas | Não permitidas (chave deve conter apenas A-Z) | Preservadas como estão (não são cifradas) |
| Números | Não permitidos (chave deve conter apenas A-Z) | Preservados como estão (não são cifrados) |
| Espaços, pontuação e demais símbolos | Não permitidos na chave | Preservados no criptograma/texto decifrado e não avançam a posição da chave |

A fórmula matemática utilizada é a clássica da Cifra de Vigenère:

- Cifração: `C = (P + K) mod 26`
- Decifração: `P = (C - K) mod 26`

onde `P` é o valor numérico da letra da mensagem, `C` a letra do criptograma e `K` a letra correspondente da chave (0 = A, 1 = B, ..., 25 = Z).

## 🕵️ Criptoanálise (Parte II)

Dado um criptograma cifrado com Vigenère e chave desconhecida, o módulo `Criptoanalise_Vigenere.py` tenta recuperar a chave e a mensagem original seguindo as etapas clássicas de ataque a esse tipo de cifra:

1. **Estimativa do tamanho da chave** — calcula o Índice de Coincidência (IC) do texto para vários tamanhos candidatos; tamanhos próximos ao real tendem a produzir um IC mais alto.
2. **Separação em subgrupos** — divide o criptograma em `m` subconjuntos (um por posição da chave), cada um cifrado com um único deslocamento fixo.
3. **Análise de frequência e comparação com o idioma** — para cada subgrupo, testa os 26 deslocamentos possíveis e escolhe o que produz a distribuição de frequência de letras mais próxima da esperada para português ou inglês (teste qui-quadrado).
4. **Reconstrução da chave e decifração** — junta a letra encontrada em cada subgrupo para formar a chave candidata e reutiliza o decifrador da Parte I para recuperar a mensagem.

## 📁 Estrutura do projeto

```
Cifra_Decifra_Vigenere.py   # Classe com a lógica de cifração e decifração (Parte I)
Criptoanalise_Vigenere.py   # Classe com a lógica do ataque de recuperação da chave (Parte II)
main.py                     # Programa de linha de comando que executa cifra, decifra e criptoanálise
teste_criptoanalise.py      # Script de teste da criptoanálise com mensagem e chave conhecidas
```

## ▶️ Como executar

Requer apenas Python 3 (nenhuma dependência externa).

```bash
python main.py
```

O programa primeiro solicita uma chave e uma mensagem, exibindo a cifração e a decifração (Parte I). Em seguida, solicita um criptograma e o idioma (português ou inglês) para executar a criptoanálise e tentar recuperar a chave e a mensagem original (Parte II).

Para testar a criptoanálise isoladamente, com uma chave e mensagem conhecidas geradas pelo próprio script:

```bash
python teste_criptoanalise.py
```

### Exemplo (Parte I)

```
Digite a chave: chave
Digite a mensagem: Ola mundo

Mensagem cifrada: QSA HYPKO
Mensagem decifrada: OLA MUNDO
```

## 👩‍💻 Desenvolvido por

- Érica Feitosa
- Isabela Furlan
- Karina Escalona
- Laíssa Soares

Estudantes do CiC - UnB

# 🔐 Cifra de Vigenère

Implementação própria da Cifra de Vigenère em Python, com cifração e decifração de mensagens a partir de uma chave textual.

Projeto desenvolvido como **Trabalho 1** da disciplina **CIC0201 - Segurança Computacional**, da Universidade de Brasília (UnB). 

## ✨ Funcionalidades

- **Cifração**: recebe uma chave e uma mensagem em texto claro e produz o criptograma correspondente.
- **Decifração**: recebe a mesma chave e o criptograma e recupera a mensagem original.
- **Validação de chave**: chaves vazias ou compostas apenas por caracteres inválidos são rejeitadas com uma mensagem de erro.
- **Normalização de acentos**: letras acentuadas são convertidas para sua forma sem acento antes do processamento (ex.: `Ç` → `C`, `Á` → `A`).
- **Suporte a números na chave**: dígitos informados na chave são convertidos para a letra correspondente do alfabeto (0 → A, 1 → B, ..., 9 → J).

## 🔤 Como o alfabeto é tratado

O alfabeto adotado é o latino de 26 letras (A-Z). As regras de processamento são:

| Tipo de caractere | Na chave | Na mensagem |
|---|---|---|
| Letras minúsculas | Convertidas para maiúsculas | Convertidas para maiúsculas |
| Letras acentuadas | Convertidas para a letra sem acento e cifradas normalmente | Convertidas para a letra sem acento e cifradas normalmente |
| Números | Convertidos para a letra correspondente (0-9 → A-J) | Preservados como estão (não são cifrados) |
| Espaços, pontuação e demais símbolos | Descartados durante a montagem da chave | Preservados no criptograma/texto decifrado e não avançam a posição da chave |

A fórmula matemática utilizada é a clássica da Cifra de Vigenère:

- Cifração: `C = (P + K) mod 26`
- Decifração: `P = (C - K) mod 26`

onde `P` é o valor numérico da letra da mensagem, `C` o da letra do criptograma e `K` o da letra correspondente da chave (0 = A, 1 = B, ..., 25 = Z).

## 📁 Estrutura do projeto

```
Cifra_Decifra_Vigenere.py   # Classe com a lógica de cifração e decifração
main.py                     # Programa de linha de comando que utiliza a classe acima
```

## ▶️ Como executar

Requer apenas Python 3 (nenhuma dependência externa).

```bash
python main.py
```

O programa solicitará a chave e a mensagem, exibindo em seguida o texto cifrado e o texto decifrado recuperado a partir dele.

### Exemplo

```
Digite a chave: chave
Digite a mensagem: Ola mundo

Mensagem cifrada: QSA HYPKO
Mensagem decifrada: OLA MUNDO
```

## 👩‍💻 Desenvolvido por

- Érica Feitosa 
- Isabela Soares
- Karina 
- Laíssa Soares

Estudantes do CiC - UnB.
# 🧠 LaTeX Logic Parser

Um analisador léxico e sintático para expressões da lógica proposicional escritas em notação LaTeX. Este projeto valida se as fórmulas estão bem formadas conforme uma gramática definida com operadores unários e binários, constantes lógicas e proposições.

---

## Funcionalidades

- Tokenização (lexer) de expressões lógicas com base em expressões regulares.
- Análise sintática (parser LL(1)) para verificação da validade das fórmulas.
- Suporte a arquivos de teste contendo múltiplas fórmulas.
- Saída formatada indicando se cada expressão é **válida** ou **inválida**.

## Regras de produção

A gramática aceita:

- **FORMULA**=CONSTANTE|PROPOSICAO|FORMULAUNARIA|FORMULABINARIA
- **CONSTANTE**=true|false.
- **PROPOSICAO**=[𝟎 − 𝟗][𝟎 − 𝟗𝒂 − 𝒛]∗
- **FORMULAUNARIA**=ABREPAREN OPERADORUNARIO FORMULA FECHAPAREN
- **FORMULABINARIA**=ABREPAREN OPERATORBINARIO FORMULA FORMULA FECHAPAREN
- **ABREPAREN**=(
- **FECHAPAREN**=)
- **OPERATORUNARIO**=\neg
- **OPERATORBINARIO**=\wedge|\vee|\rightarrow|\leftrightarrow


### Exemplos de expressões válidas:

```latex
(\wedge 1x true)
(\neg (1y))
(\rightarrow 2a (\vee false 1b))
´´´

## Como Executar
- 1 Clonando o repositório

```bash
$ git clone https://github.com/leonardofalango/latex_parser.git
$ cd latex_parser
```

- 2 Executando o parser
```bash
$ python3.11 main.py
```
Isso rodará os 3 arquivos de teste que estão localizados na pasta test_files/

- 3 Executando o parser com um arquivo de entrada
```bash
$ python3.11 main.py <caminho do arquivo>.txt
```

- 4 Executando com mais de um arquivo de entrada
```bash
$ python3.11 main.py <caminho1>.txt <caminho2>.txt ...
```

- ### Para não processar os arquivos de teste, basta adicionar um argumento hide
```bash
$ python3.11 main.py hide <caminho do arquivo>.txt
```
Com múltiplos arquivos:
```bash
$ python3.11 main.py hide <caminho1>.txt <caminho2>.txt ...
```

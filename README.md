# Jogo da Forca

Este repositório contém um jogo da forca desenvolvido em Python. O jogo é uma implementação simples e interativa do clássico jogo de adivinhação de palavras, onde o jogador tem um número limitado de tentativas para adivinhar a palavra correta. O projeto inclui funcionalidades como registro de pontuações, exibição de scores e uma interface de menu para facilitar a navegação. Feito para aula prática de Lógica de Programação e Algoritmos do curso de Análise e Desenvolvimento de Sistemas da UNINTER.

## Como Jogar

- **Clone o repositório**:
```bash
git clone https://github.com/felixnogueira/jogo_forca.git
```
- **Navegue até o diretório do projeto**:
```bash
cd jogo_forca
```
- **Execute o jogo**:
```bash
python main.py
```
- **Siga as instruções**:
    
    - No menu principal, escolha a opção **"1 - JOGAR"** para iniciar o jogo.
        
    - Digite seu nome quando solicitado.
        
    - Tente adivinhar a palavra secreta digitando letras.
        
    - Você tem 6 tentativas para acertar a palavra. Caso erre, o boneco da forca será desenhado gradualmente.
        
    - Se você acertar a palavra, ganha pontos com base no número de erros cometidos.
        
    - Se errar todas as tentativas, o jogo termina e a palavra secreta é revelada.
        

## Estrutura do Projeto

O projeto é composto pelos seguintes arquivos:

- **`artwork.py`**: Contém funções para exibir a palavra secreta com letras ocultas e desenhar o boneco da forca com base no número de erros.
    
- **`fileHandler.py`**: Responsável por manipular arquivos, como verificar a existência de arquivos, ler e escrever dados (por exemplo, scores dos jogadores).
    
- **`game.py`**: Contém a lógica principal do jogo, incluindo a seleção de palavras aleatórias e o controle das tentativas do jogador.
    
- **`main.py`**: O ponto de entrada do programa, que exibe o menu principal e gerencia as opções do usuário (jogar, ver scores ou sair).
    
- **`palavras.txt`**: Um arquivo de texto contendo uma lista de palavras que podem ser sorteadas como palavras secretas.
    
- **`score.txt`**: Armazena os scores dos jogadores no formato `nome;pontuação`.
    

## Requisitos

- Python 3.x

## Como Funciona

1. **Menu Principal**:
    
    - Ao executar o programa, o menu principal é exibido com as opções:
        
        - **1 - JOGAR**: Inicia o jogo da forca.
            
        - **2 - SCORE**: Exibe a lista de pontuações dos jogadores.
            
        - **3 - SAIR**: Encerra o programa.
            
2. **Jogo**:
    
    - O jogo seleciona uma palavra aleatória do arquivo `palavras.txt`.
        
    - O jogador digita letras para tentar adivinhar a palavra.
        
    - A cada erro, o boneco da forca é desenhado, e o número de tentativas restantes diminui.
        
    - A pontuação é calculada com base no número de erros cometidos.
        
3. **Scores**:
    
    - As pontuações dos jogadores são armazenadas no arquivo `score.txt`.
        
    - O jogador pode visualizar os scores anteriores na opção "SCORE" do menu.
  

## TO-DO:

    - Trocar armazenamento do score em arquivo de texto para banco de dados (sqlite3)

    - Utilizar a biblioteca pygame para criar interface gráfica

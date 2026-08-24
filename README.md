# 🛡️ Simulador de Combate Modular em Python

Projeto educacional desenvolvido para o ensino de programação orientada a módulos, separação de responsabilidades, importação de arquivos e lógica de jogos em Python. Ideal para aulas de cursos técnicos de desenvolvimento de sistemas.

---

## 📂 Arquitetura do Projeto

O código está estruturado de forma modular para demonstrar aos alunos como organizar um projeto do mundo real:

```text
projeto_rpg/
│
├── personagem/
│   ├── ficha.py        # Coleta dados do usuário, calcula HP e MP baseados em ATK, DEF e EVA.
│   └── logJogo.py      # Gerencia o histórico e o diário de bordo das ações do jogo.
│
├── mestre/
│   └── inimigos.py     # Contém a lista de monstros e o cadastro de oponentes.
│
├── funcoes.py          # Centraliza as regras matemáticas, rolagem de d20 e cálculo de dano.
└── main.py             # Arquivo principal que importa os módulos e executa o Game Loop.



# Como Executar e Testar
Certifique-se de ter o Python 3.10+ instalado na sua máquina.

Clone este repositório ou baixe os arquivos mantendo a mesma árvore de diretórios apresentada acima.

Abra o terminal (ou VS Code) na pasta raiz do projeto.

Execute o arquivo principal digitando:

Bash
python main.py

# Siga as instruções no terminal:

Digite o nome do seu herói e distribua/insira seus atributos (ATK, DEF, EVA).
Escolha qual monstro deseja enfrentar na lista gerada pelo Mestre.
Utilize as opções de combate para atacar e testar a rolagem dos dados baseada no d20.

# Conceitos Didáticos Aplicados

Modularização: Como isolar lógicas em arquivos separados utilizando pastas e subpastas (from pasta.arquivo import funcao).
Estruturas de Dados: Uso intensivo de Dicionários (dict) para modelar personagens e inimigos, e Listas (list) para registros e logs.
Game Loop e Condicionais: Utilização de laços while e estruturas if-elif-else para controlar o fluxo de vida e turnos.
Randomização: Uso da biblioteca nativa random para simular a imprevisibilidade de um RPG de mesa tradicional.
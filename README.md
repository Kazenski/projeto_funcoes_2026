# 🛡️ Simulador de Combate Modular em Python

Projeto educacional desenvolvido para o ensino de programação orientada a módulos, separação de responsabilidades, importação de arquivos e lógica de jogos em Python. Ideal para aulas de cursos técnicos de desenvolvimento de sistemas.

---

## 📂 Arquitetura do Projeto

O código está estruturado de forma modular para demonstrar aos alunos como organizar um projeto do mundo real:

projeto_rpg/
│
├── personagem/
│   ├── ficha.py          # Coleta dados e gerencia o inventário/equipamentos do herói
│   └── logJogo.py        # Logs e exportação em TXT
│
├── mestre/
│   └── supabase_mestre.py# Funções para buscar monstros e itens direto do Supabase
│
├── funcoes.py            # Regras matemáticas, d20 e narrativa
├── conexao.py            # Credenciais e conexão com o Supabase
└── main.py               # Game Loop principal



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


# Como Conectar o Python ao Supabase
Para conectar o projeto ao Supabase, utilizamos a biblioteca oficial do Python chamada supabase.

# Passo a passo para os alunos:
No terminal do VS Code, instalar a biblioteca oficial:

Bash
pip install supabase
python.exe -m pip install --upgrade pip
No painel do Supabase: Criar um projeto, ir nas configurações (Project Settings > API) e copiar a URL do projeto e a chave secreta anon public (ou service_role).

Para evitar expor chaves de segurança no GitHub, ensinamos os alunos a usarem variáveis de ambiente ou a criarem um arquivo de configuração isolado (conexao.py).
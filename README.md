# Simulador de Combate Modular em Python

Projeto educacional desenvolvido para o ensino de programação orientada a módulos, separação de responsabilidades, importação de arquivos e lógica de jogos em Python. Ideal para aulas de cursos técnicos de desenvolvimento de sistemas.

## Arquitetura do Projeto

O código está estruturado de forma modular para demonstrar aos alunos como organizar um projeto do mundo real:

```
projeto_rpg/
│
├── personagem/
│   ├── ficha.py          # Coleta dados e gerencia inventário/equipamentos do herói
│   └── logJogo.py        # Logs e exportação em TXT
├── mestre/
│   └── supabase_mestre.py# Busca monstros e itens direto do Supabase
│
├── funcoes.py            # Regras matemáticas, d20 e narrativa
├── conexao.py            # Credenciais e conexão com o Supabase
└── main.py               # Game Loop principal
```

# Como Executar e Testar
Certifique-se de ter o Python 3.10+ instalado na sua máquina.

Clone este repositório ou baixe os arquivos mantendo a mesma árvore de diretórios apresentada acima.

Abra o terminal (ou VS Code) na pasta raiz do projeto.

Execute o arquivo principal digitando:

```
Bash
python main.py
```

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

```
pip install supabase
python.exe -m pip install --upgrade pip
```

No painel do Supabase: Criar um projeto, ir nas configurações (Project Settings > API) e copiar a URL do projeto e a chave secreta anon public (ou service_role).

Para evitar expor chaves de segurança no GitHub, ensinamos os alunos a usarem variáveis de ambiente ou a criarem um arquivo de configuração isolado (conexao.py).

# Configurações do Supabase:
Primeiro crie um projeto, dando-lhe um nome.
<img width="1398" height="571" alt="image" src="https://github.com/user-attachments/assets/afdfaed6-b2dc-489a-82e5-9dd9583e1439" />

Vamos encontrar as credenciais para conectar o nosso Código Python ao Supabase:
<img width="1577" height="821" alt="image" src="https://github.com/user-attachments/assets/435ff5e8-aa49-41c2-8293-ab4517b11b70" />

Agora procure pelo Project URL conforme a imagem:
<img width="1551" height="581" alt="image" src="https://github.com/user-attachments/assets/c3d678d5-c5d4-4fd7-9d4a-f6731151a667" />

Agora procure pela credencial conforme as imagens:
<img width="1605" height="729" alt="image" src="https://github.com/user-attachments/assets/fa953bf8-948c-45aa-8ae6-c307ee0a217b" />

<img width="1114" height="522" alt="image" src="https://github.com/user-attachments/assets/09e571de-fc81-40ef-95f5-c212947a8ab6" />

<img width="1279" height="550" alt="image" src="https://github.com/user-attachments/assets/68fbd561-63f4-4c90-bcf6-fb0c2ce4ebc9" />

Agora crie a estrutura da sua base de dados:

<img width="1730" height="831" alt="image" src="https://github.com/user-attachments/assets/585e2e4a-eddc-405c-abf9-1225219ac14f" />

<img width="1872" height="914" alt="image" src="https://github.com/user-attachments/assets/f84ee9ee-e2e7-43bd-b840-9b52b25fcbd4" />

Cole o seguinte código para criar a estrutura das entidades, atributos, seus tipos e esquemas necessários:

```
-- 1. Tabela de Inimigos cadastrados pelo Mestre
CREATE TABLE inimigos (
    id SERIAL PRIMARY KEY,
    nome TEXT NOT NULL,
    atk INT NOT NULL,
    def INT NOT NULL,
    hp INT NOT NULL
);

-- 2. Tabela de Equipamentos disponíveis (Itens que modificam atributos)
CREATE TABLE equipamentos (
    id SERIAL PRIMARY KEY,
    nome TEXT NOT NULL,
    bonus_atk INT DEFAULT 0,
    bonus_def INT DEFAULT 0,
    bonus_eva INT DEFAULT 0
);

-- 3. Inserindo dados iniciais de exemplo para testes
INSERT INTO inimigos (nome, atk, def, hp) VALUES 
('Goblin Ladrão', 12, 4, 30),
('Orc Guerreiro', 18, 8, 60),
('Dragão de Fogo', 35, 15, 150);

INSERT INTO equipamentos (nome, bonus_atk, bonus_def, bonus_eva) VALUES 
('Espada de Ferro', 5, 0, 0),
('Escudo de Madeira', 0, 8, -2),
('Capacete Ágil', 0, 2, 5);
```
<img width="1843" height="917" alt="image" src="https://github.com/user-attachments/assets/6024d8d2-646c-4145-85f3-e5606bf96207" />

<img width="693" height="894" alt="image" src="https://github.com/user-attachments/assets/913622dd-9efe-4411-86ee-295f22895f54" />

Você deverá ter visto a seguinte mensagem: "Success. No rows returned."





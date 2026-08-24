# =============================================================================
# ARQUIVO: personagem/ficha.py
# OBJETIVO: Coletar atributos do jogador e calcular HP e MP baseados neles.
# =============================================================================

def criar_ficha():
    print("-" * 40)
    print(f"{'CRIACAO DA FICHA DO PERSONAGEM':^40}")
    print("-" * 40)
    
    nome = input("Digite o nome do seu herói: ")
    
    # Coletando atributos básicos digitados pelo usuário
    atk = int(input("Digite o ATK (Ataque): "))
    def_val = int(input("Digite a DEF (Defesa): "))
    eva = int(input("Digite a EVA (Evasiva): "))
    
    # Atributos derivados para dar mais dinamismo ao RPG
    hp = 100 + (def_val * 5)  # Cada ponto de DEF aumenta a vida
    mp = 50 + (atk * 2)       # Cada ponto de ATK aumenta a magia
    
    # Criando o dicionário que representa a ficha do personagem
    ficha_personagem = {
        "nome": nome,
        "ATK": atk,
        "DEF": def_val,
        "EVA": eva,
        "HP": hp,
        "MP": mp,
        "HP_ATUAL": hp
    }
    
    print("-" * 40)
    print("Ficha criada com sucesso!")
    print("-" * 40)
    
    return ficha_personagem
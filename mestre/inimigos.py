# =============================================================================
# ARQUIVO: mestre/inimigos.py
# OBJETIVO: Cadastrar e fornecer os inimigos do jogo.
# =============================================================================

def obter_lista_inimigos():
    inimigos = [
        {"nome": "Goblin Ladrão", "ATK": 12, "DEF": 4, "HP": 30},
        {"nome": "Orc Guerreiro", "ATK": 18, "DEF": 8, "HP": 60},
        {"nome": "Esqueletão Mago", "ATK": 22, "DEF": 5, "HP": 45},
        {"nome": "Dragão de Fogo", "ATK": 35, "DEF": 15, "HP": 150}
    ]
    return inimigos

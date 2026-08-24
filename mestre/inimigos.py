# =============================================================================
# ARQUIVO: mestre/inimigos.py
# OBJETIVO: Cadastrar e gerenciar a lista de inimigos do jogo.
# =============================================================================

def obter_lista_inimigos():
    """Retorna uma lista de dicionários contendo os monstros disponíveis."""
    inimigos = [
        {"nome": "Goblin Ladrão", "ATK": 12, "DEF": 4, "HP": 30},
        {"nome": "Orc Guerreiro", "ATK": 18, "DEF": 8, "HP": 60},
        {"nome": "Esqueletão Mago", "ATK": 22, "DEF": 5, "HP": 45},
        {"nome": "Dragão de Fogo", "ATK": 35, "DEF": 15, "HP": 150}
    ]
    return inimigos

def selecionar_inimigo(indice):
    """Seleciona um inimigo específico com base na escolha numérica."""
    lista = obter_lista_inimigos()
    if 0 <= indice < len(lista):
        return lista[indice]
    return lista[0] # Retorna o primeiro por segurança (Fallback)
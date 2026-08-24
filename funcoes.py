# =============================================================================
# ARQUIVO: funcoes.py
# OBJETIVO: Centralizar funções gerais de mecânica de jogo (rolagem de dados, ataque).
# =============================================================================

import random

def rolar_d20():
    """Simula a rolagem de um dado de 20 faces (1 a 20)."""
    return random.randint(1, 20)

def calcular_ataque(atk_personagem, def_inimigo):
    """
    Calcula o dano do ataque utilizando a rolagem do d20 como fator de sorte.
    """
    dado = rolar_d20()
    print(f"🎲 Dado de 20 faces rodado... Caiu no número: {dado}")
    
    # Se tirar 1, é falha crítica (dano zero)
    if dado == 1:
        print("💥 Falha Crítica! O ataque errou feio.")
        return 0, dado
        
    # Se tirar 20, é acerto crítico (dano dobrado)
    elif dado == 20:
        print("⚡ ACERTO CRÍTICO! Dano dobrado!")
        dano = (atk_personagem * 2) - def_inimigo
        return max(dano, 1), dado
        
    # Ataque normal
    else:
        dano = (atk_personagem + dado) - def_inimigo
        return max(dano, 1), dado # Garante pelo menos 1 de dano se acertar
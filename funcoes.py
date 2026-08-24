# =============================================================================
# ARQUIVO: funcoes.py
# OBJETIVO: Centralizar rolagem de dados, cálculo de ataque e narração textual.
# =============================================================================

import random


def rolar_d20():
    """Simula a rolagem de um dado de 20 faces (1 a 20)."""
    return random.randint(1, 20)


def calcular_ataque(atk_atacante, def_defensor):
    """Calcula o dano bruto utilizando o d20 e retorna o dano e o valor do dado."""
    dado = rolar_d20()

    if dado == 1:
        return 0, dado  # Falha crítica
    elif dado == 20:
        dano = (atk_atacante * 2) - def_defensor
        return max(dano, 2), dado  # Crítico (garante dano mínimo 2)
    else:
        dano = (atk_atacante + dado) - def_defensor
        return max(dano, 1), dado  # Ataque normal (garante dano mínimo 1)


def gerar_narrativa_ataque(nome_atacante, nome_defensor, dano, valor_d20):
    """
    Função dedicada exclusivamente a traduzir os números em uma 
    descrição textual rica para o jogador (Isolando a lógica de texto).
    """
    if valor_d20 == 1:
        return f"💥 {nome_atacante} tentou atacar {nome_defensor}, mas tirou 1 no d20 e tropeçou! Errou feio (0 de dano)."
    elif valor_d20 == 20:
        return f"⚡ CRÍTICO! {nome_atacante} acertou um golpe devastador em {nome_defensor}, rasgando defesas e causando {dano} de dano!"
    elif dano <= 2:
        return f"🛡️ {nome_defensor} conseguiu amortecer o impacto do ataque de {nome_atacante}. Dano leve: {dano}."
    else:
        return f"⚔️ {nome_atacante} superou a defesa de {nome_defensor} com um bom golpe e causou {dano} pontos de dano."

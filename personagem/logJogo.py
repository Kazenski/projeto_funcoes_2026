# =============================================================================
# ARQUIVO: personagem/logJogo.py
# OBJETIVO: Armazenar e exibir o histórico de eventos das partidas.
# =============================================================================

# Lista global para armazenar os registros do jogo
historico_combate = []

def registrar_acao(detalhe):
    """Adiciona um novo evento/log na lista de histórico."""
    historico_combate.append(detalhe)

def exibir_historico():
    """Imprime todo o log do que aconteceu no jogo até o momento."""
    print("\n" + "=" * 40)
    print(f"{'DIÁRIO DE BORDO / LOG DO JOGO':^40}")
    print("=" * 40)
    
    if len(historico_combate) == 0:
        print("Nenhuma ação registrada ainda.")
    else:
        for i, evento in enumerate(historico_combate, 1):
            print(f"[{i:02d}] {evento}")
            
    print("=" * 40 + "\n")
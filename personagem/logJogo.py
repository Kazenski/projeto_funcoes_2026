# =============================================================================
# ARQUIVO: personagem/logJogo.py
# OBJETIVO: Armazenar histórico de combate e exportar para arquivo TXT.
# =============================================================================

historico_combate = []


def registrar_acao(detalhe):
    """Adiciona um novo evento/log na lista global de histórico."""
    historico_combate.append(detalhe)


def exibir_historico():
    """Imprime todo o log do que aconteceu no jogo no terminal."""
    print("\n" + "=" * 40)
    print(f"{'DIÁRIO DE BORDO / LOG DO JOGO':^40}")
    print("=" * 40)

    if len(historico_combate) == 0:
        print("Nenhuma ação registrada ainda.")
    else:
        for i, evento in enumerate(historico_combate, 1):
            print(f"[{i:02d}] {evento}")

    print("=" * 40 + "\n")


def exportar_historico_txt():
    """Exporta o diário de bordo completo para um arquivo de texto (.txt)."""
    with open("diario_bordo_combate.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("=" * 50 + "\n")
        arquivo.write(f"{'RELATÓRIO DE BATALHA - DIÁRIO DE BORDO':^50}\n")
        arquivo.write("=" * 50 + "\n\n")

        for i, evento in enumerate(historico_combate, 1):
            arquivo.write(f"[{i:02d}] {evento}\n")

        arquivo.write("\n" + "=" * 50 + "\n")

    print("📁 Diário de bordo exportado com sucesso para 'diario_bordo_combate.txt'!")

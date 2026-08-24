# =============================================================================
# ARQUIVO: main.py
# OBJETIVO: Orquestrar o jogo, o loop de turnos e a exportação final de arquivos.
# =============================================================================

from personagem.ficha import criar_ficha, exportar_ficha_txt
from personagem.logJogo import registrar_acao, exibir_historico, exportar_historico_txt
from mestre.inimigos import obter_lista_inimigos
from funcoes import calcular_ataque, gerar_narrativa_ataque


def iniciar_jogo():
    print("-" * 50)
    print(f"{'SIMULADOR DE COMBATE RPG - MODULAR':^50}")
    print("-" * 50)

    # 1. Criação do personagem
    heroi = criar_ficha()
    registrar_acao(
        f"Herói {heroi['nome']} entrou na masmorra com ATK:{heroi['ATK']} DEF:{heroi['DEF']}")

    # 2. Escolha do Inimigo
    print("\nEscolha seu oponente:")
    inimigos = obter_lista_inimigos()
    for i, inimigo in enumerate(inimigos):
        print(
            f"[{i}] {inimigo['nome']} (HP: {inimigo['HP']} | ATK: {inimigo['ATK']} | DEF: {inimigo['DEF']})")

    escolha = int(input("Digite o número do inimigo que deseja enfrentar: "))
    alvo = inimigos[escolha].copy()

    registrar_acao(f"Combate iniciado contra o chefe: {alvo['nome']}")

    # 3. Loop de Combate
    while heroi["HP_ATUAL"] > 0 and alvo["HP"] > 0:
        print("\n" + "-" * 40)
        print(
            f"STATUS -> {heroi['nome']} (HP: {heroi['HP_ATUAL']}) X {alvo['nome']} (HP: {alvo['HP']})")
        print("-" * 40)

        acao = input(
            "Deseja [1] Atacar, [2] Ver Log na Tela ou [3] Sair/Fugir? ").strip()

        if acao == "1":
            print(f"\nTurno de {heroi['nome']}:")
            dano_heroi, d20_heroi = calcular_ataque(heroi["ATK"], alvo["DEF"])
            alvo["HP"] -= dano_heroi
            alvo["HP"] = max(alvo["HP"], 0)  # Impede HP negativo na exibição

            # Usando a nova função modular de narrativa
            texto_ataque_heroi = gerar_narrativa_ataque(
                heroi['nome'], alvo['nome'], dano_heroi, d20_heroi)
            print(texto_ataque_heroi)
            registrar_acao(texto_ataque_heroi)

            # Checa se o inimigo morreu
            if alvo["HP"] == 0:
                print(
                    f"\n🏆 GLÓRIA! {alvo['nome']} foi completamente derrotado!")
                registrar_acao(
                    f"Vitória! {heroi['nome']} derrotou {alvo['nome']}.")
                break

            # Turno do Inimigo (Retruca)
            print(f"\nTurno de {alvo['nome']}:")
            dano_inimigo, d20_inimigo = calcular_ataque(
                alvo["ATK"], heroi["DEF"])
            heroi["HP_ATUAL"] -= dano_inimigo
            heroi["HP_ATUAL"] = max(heroi["HP_ATUAL"], 0)

            texto_ataque_inimigo = gerar_narrativa_ataque(
                alvo['nome'], heroi['nome'], dano_inimigo, d20_inimigo)
            print(texto_ataque_inimigo)
            registrar_acao(texto_ataque_inimigo)

            if heroi["HP_ATUAL"] == 0:
                print(
                    f"\n💀 DERROTA... {heroi['nome']} caiu em batalha perante {alvo['nome']}.")
                registrar_acao(
                    f"Derrota. {heroi['nome']} foi abatido por {alvo['nome']}.")
                break

        elif acao == "2":
            exibir_historico()
        elif acao == "3":
            print("Você fugiu da batalha tchê! Fim de jogo antecipado.")
            registrar_acao(
                f"{heroi['nome']} fugiu do combate contra {alvo['nome']}.")
            break
        else:
            print("Opção inválida!")

    # 4. Finalização e Exportação de Arquivos em TXT
    print("\n" + "=" * 50)
    print("GERANDO ARQUIVOS DE REGISTRO DO JOGO...")
    print("=" * 50)
    exportar_ficha_txt(heroi)
    exportar_historico_txt()
    print("Processo finalizado com sucesso! Confira os arquivos .txt gerados na pasta.")


if __name__ == "__main__":
    iniciar_jogo()

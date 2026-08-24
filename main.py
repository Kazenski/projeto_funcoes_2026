# =============================================================================
# ARQUIVO: main.py
# OBJETIVO: Integrar banco de dados Supabase, equipamentos e o loop de combate.
# =============================================================================

from personagem.ficha import criar_ficha, equipar_item, calcular_atributos_totais
from personagem.logJogo import registrar_acao, exibir_historico, exportar_historico_txt
from mestre.supabase_mestre import obter_inimigos_do_banco, obter_equipamentos_do_banco, cadastrar_novo_inimigo
from funcoes import calcular_ataque, gerar_narrativa_ataque


def iniciar_jogo():
    print("-" * 50)
    print(f"{'SUPABASE RPG - COMBATE MODULAR COM CLOUD DB':^50}")
    print("-" * 50)

    # 1. Criar Herói
    heroi = criar_ficha()

    # 2. Buscar Equipamentos no Supabase e permitir escolher um
    print("\n📦 Conectando ao Supabase para buscar equipamentos disponíveis...")
    itens_loja = obter_equipamentos_do_banco()

    if itens_loja:
        print("\nEscolha um equipamento inicial:")
        for i, item in enumerate(itens_loja):
            print(
                f"[{i}] {item['nome']} (ATK: +{item['bonus_atk']}, DEF: +{item['bonus_def']}, EVA: +{item['bonus_eva']})")

        op_item = int(input("Digite o número do item desejado: "))
        if 0 <= op_item < len(itens_loja):
            equipar_item(heroi, itens_loja[op_item])

    # 3. Buscar Inimigos no Supabase
    print("\n👾 Buscando lista de chefes no Supabase...")
    inimigos = obter_inimigos_do_banco()

    if not inimigos:
        print("Nenhum inimigo encontrado no banco. Cadastrando um padrão de emergência...")
        inimigos = [{"nome": "Goblin de Emergência",
                     "atk": 10, "def": 2, "hp": 25}]

    print("\nEscolha seu oponente:")
    for i, inimigo in enumerate(inimigos):
        print(
            f"[{i}] {inimigo['nome']} (HP: {inimigo['hp']} | ATK: {inimigo['atk']} | DEF: {inimigo['def']})")

    escolha = int(input("Digite o número do inimigo para lutar: "))
    alvo = inimigos[escolha].copy()  # Cópia para manipular o HP localmente

    registrar_acao(f"Combate iniciado: {heroi['nome']} vs {alvo['nome']}")

    # 4. Loop de Combate utilizando atributos com equipamentos
    while heroi["HP_ATUAL"] > 0 and alvo["hp"] > 0:
        atk_real, def_real, eva_real = calcular_atributos_totais(heroi)

        print("\n" + "-" * 40)
        print(
            f"STATUS -> {heroi['nome']} (HP: {heroi['HP_ATUAL']}) X {alvo['nome']} (HP: {alvo['hp']})")
        print(
            f"Efetivos -> ATK: {atk_real} | DEF: {def_real} | EVA: {eva_real}")
        print("-" * 40)

        acao = input(
            "Deseja [1] Atacar, [2] Ver Log ou [3] Cadastrar Novo Monstro no DB? ").strip()

        if acao == "1":
            # Turno do Herói
            dano_heroi, d20_heroi = calcular_ataque(atk_real, alvo["def"])
            alvo["hp"] -= dano_heroi
            alvo["hp"] = max(alvo["hp"], 0)

            texto1 = gerar_narrativa_ataque(
                heroi['nome'], alvo['nome'], dano_heroi, d20_heroi)
            print(texto1)
            registrar_acao(texto1)

            if alvo["hp"] == 0:
                print(f"\n🏆 Vitória! {alvo['nome']} foi destruído!")
                registrar_acao(f"Herói venceu {alvo['nome']}.")
                break

            # Turno do Inimigo
            dano_inimigo, d20_inimigo = calcular_ataque(alvo["atk"], def_real)
            heroi["HP_ATUAL"] -= dano_inimigo
            heroi["HP_ATUAL"] = max(heroi["HP_ATUAL"], 0)

            texto2 = gerar_narrativa_ataque(
                alvo['nome'], heroi['nome'], dano_inimigo, d20_inimigo)
            print(texto2)
            registrar_acao(texto2)

            if heroi["HP_ATUAL"] == 0:
                print(f"\n💀 DERROTA... Você foi abatido.")
                registrar_acao(f"Herói derrotado por {alvo['nome']}.")
                break

        elif acao == "2":
            exibir_historico()
        elif acao == "3":
            print("\n--- PAINEL DO MESTRE: CADASTRAR NO SUPABASE ---")
            m_nome = input("Nome do monstro: ")
            m_atk = int(input("ATK: "))
            m_def = int(input("DEF: "))
            m_hp = int(input("HP: "))
            cadastrar_novo_inimigo(m_nome, m_atk, m_def, m_hp)
            print(
                "Monstro salvo na nuvem com sucesso! Reinicie o combate para encontrá-lo.")
        else:
            print("Opção inválida!")

    exportar_historico_txt()


if __name__ == "__main__":
    iniciar_jogo()

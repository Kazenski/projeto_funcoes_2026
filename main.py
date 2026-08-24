# =============================================================================
# ARQUIVO: main.py
# OBJETIVO: Integrar todos os módulos (ficha, log, inimigos, funções) em um loop.
# =============================================================================

from personagem.ficha import criar_ficha
from personagem.logJogo import registrar_acao, exibir_historico
from mestre.inimigos import obter_lista_inimigos
from funcoes import calcular_ataque

def iniciar_jogo():
    print("-" * 50)
    print(f"{'BEM-VINDO AO SIMULADOR DE COMBATE RPG':^50}")
    print("-" * 50)
    
    # 1. Criação do personagem
    heroi = criar_ficha()
    registrar_acao(f"Herói {heroi['nome']} entrou na masmorra com ATK:{heroi['ATK']} DEF:{heroi['DEF']}")
    
    # 2. Escolha do Inimigo
    print("\nEscolha seu oponente:")
    inimigos = obter_lista_inimigos()
    for i, inimigo in enumerate(inimigos):
        print(f"[{i}] {inimigo['nome']} (HP: {inimigo['HP']} | ATK: {inimigo['ATK']} | DEF: {inimigo['DEF']})")
        
    escolha = int(input("Digite o número do inimigo que deseja enfrentar: "))
    alvo = inimigos[escolha].copy() # Cópia para não alterar a lista original permanentemente
    
    registrar_acao(f"Combate iniciado contra: {alvo['nome']}")
    
    # 3. Loop de Combate Simples
    while heroi["HP_ATUAL"] > 0 and alvo["HP"] > 0:
        print("\n" + "-" * 30)
        print(f"STATUS -> {heroi['nome']} (HP: {heroi['HP_ATUAL']}) X {alvo['nome']} (HP: {alvo['HP']})")
        print("-" * 30)
        
        acao = input("Deseja [1] Atacar ou [2] Ver Log de Batalha? ").strip()
        
        if acao == "1":
            print(f"\n{heroi['nome']} ataca {alvo['nome']}!")
            dano_causado, valor_d20 = calcular_ataque(heroi["ATK"], alvo["DEF"])
            
            alvo["HP"] -= dano_causado
            print(f"-> Causou {dano_causado} de dano! (Dado d20: {valor_d20})")
            registrar_acao(f"{heroi['nome']} atacou {alvo['nome']} tirando {dano_causado} de HP (d20: {valor_d20}).")
            
            # Turno do inimigo se ele continuar vivo
            if alvo["HP"] > 0:
                print(f"\n{alvo['nome']} retruca o ataque!")
                dano_recebido, dado_inimigo = calcular_ataque(alvo["ATK"], heroi["DEF"])
                heroi["HP_ATUAL"] -= dano_recebido
                print(f"-> Você recebeu {dano_recebido} de dano! (Dado d20: {dado_inimigo})")
                registrar_acao(f"{alvo['nome']} retrucou tirando {dano_recebido} do herói.")
            else:
                print(f"\n🏆 Vitória! {alvo['nome']} foi derrotado!")
                registrar_acao(f"Herói {heroi['nome']} venceu o combate contra {alvo['nome']}.")
                
        elif acao == "2":
            exibir_historico()
        else:
            print("Opção inválida! Escolha 1 ou 2.")
            
    print("\nFim de jogo. Obrigado por testar o simulador modular!")
    exibir_historico()

if __name__ == "__main__":
    iniciar_jogo()
# =============================================================================
# ARQUIVO: personagem/ficha.py
# OBJETIVO: Gerenciar atributos, HP, MP e o equipamento ativo do herói.
# =============================================================================

def criar_ficha():
    print("-" * 40)
    print(f"{'CRIACAO DA FICHA DO PERSONAGEM':^40}")
    print("-" * 40)

    nome = input("Digite o nome do seu herói: ")
    atk = int(input("Digite o ATK base: "))
    def_val = int(input("Digite a DEF base: "))
    eva = int(input("Digite a EVA base: "))

    hp = 100 + (def_val * 5)
    mp = 50 + (atk * 2)

    ficha_personagem = {
        "nome": nome,
        "ATK_BASE": atk,
        "DEF_BASE": def_val,
        "EVA_BASE": eva,
        "HP_MAX": hp,
        "HP_ATUAL": hp,
        "MP": mp,
        "equipamento": None  # Começa sem equipamento
    }

    print("-" * 40)
    print("Ficha criada com sucesso!")
    print("-" * 40)
    return ficha_personagem


def equipar_item(ficha, item):
    """Equipa um item no personagem, modificando seus atributos efetivos."""
    ficha["equipamento"] = item
    print(f"\n🎒 {ficha['nome']} equipou: {item['nome']}!")
    print(
        f"   Bônus -> ATK: +{item['bonus_atk']} | DEF: +{item['bonus_def']} | EVA: +{item['bonus_eva']}")


def calcular_atributos_totais(ficha):
    """Retorna os atributos reais considerando o equipamento ativo."""
    if not ficha["equipamento"]:
        return ficha["ATK_BASE"], ficha["DEF_BASE"], ficha["EVA_BASE"]

    item = ficha["equipamento"]
    atk_total = ficha["ATK_BASE"] + item["bonus_atk"]
    def_total = ficha["DEF_BASE"] + item["bonus_def"]
    eva_total = ficha["EVA_BASE"] + item["bonus_eva"]

    return atk_total, def_total, eva_total

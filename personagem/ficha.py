# =============================================================================
# ARQUIVO: personagem/ficha.py
# OBJETIVO: Coletar atributos, calcular derivados e permitir exportação em TXT.
# =============================================================================

def criar_ficha():
    print("-" * 40)
    print(f"{'CRIACAO DA FICHA DO PERSONAGEM':^40}")
    print("-" * 40)

    nome = input("Digite o nome do seu herói: ")
    atk = int(input("Digite o ATK (Ataque): "))
    def_val = int(input("Digite a DEF (Defesa): "))
    eva = int(input("Digite a EVA (Evasiva): "))

    hp = 100 + (def_val * 5)
    mp = 50 + (atk * 2)

    ficha_personagem = {
        "nome": nome,
        "ATK": atk,
        "DEF": def_val,
        "EVA": eva,
        "HP_MAX": hp,
        "HP_ATUAL": hp,
        "MP": mp
    }

    print("-" * 40)
    print("Ficha criada com sucesso!")
    print("-" * 40)

    return ficha_personagem


def exportar_ficha_txt(ficha):
    """Salva os dados finais atualizados do personagem em um arquivo de texto."""
    nome_arquivo = f"ficha_{ficha['nome'].lower().replace(' ', '_')}.txt"

    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        arquivo.write("=" * 40 + "\n")
        arquivo.write(f"FICHA FINAL DE PERSONAGEM: {ficha['nome']}\n")
        arquivo.write("=" * 40 + "\n")
        arquivo.write(f"ATK (Ataque): {ficha['ATK']}\n")
        arquivo.write(f"DEF (Defesa): {ficha['DEF']}\n")
        arquivo.write(f"EVA (Evasiva): {ficha['EVA']}\n")
        arquivo.write(f"HP Final: {ficha['HP_ATUAL']} / {ficha['HP_MAX']}\n")
        arquivo.write(f"MP Final: {ficha['MP']}\n")
        arquivo.write("=" * 40 + "\n")

    print(f"📁 Ficha salva com sucesso no arquivo: {nome_arquivo}")

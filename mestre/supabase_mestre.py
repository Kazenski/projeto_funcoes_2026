# =============================================================================
# ARQUIVO: mestre/supabase_mestre.py
# OBJETIVO: Buscar dados de inimigos e itens diretamente do Supabase.
# =============================================================================

from conexao import conectar_supabase


def obter_inimigos_do_banco():
    """Busca a lista de inimigos cadastrados no Supabase."""
    db = conectar_supabase()
    if not db:
        return []

    resposta = db.table("inimigos").select("*").execute()
    return resposta.data


def obter_equipamentos_do_banco():
    """Busca a lista de itens/equipamentos disponíveis no Supabase."""
    db = conectar_supabase()
    if not db:
        return []

    resposta = db.table("equipamentos").select("*").execute()
    return resposta.data


def cadastrar_novo_inimigo(nome, atk, def_val, hp):
    """Permite ao mestre cadastrar um novo monstro direto no Supabase."""
    db = conectar_supabase()
    if not db:
        return False

    dados = {"nome": nome, "atk": atk, "def": def_val, "hp": hp}
    db.table("inimigos").insert(dados).execute()
    print(f"✨ Inimigo '{nome}' cadastrado com sucesso no Supabase!")
    return True

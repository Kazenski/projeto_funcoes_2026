# =============================================================================
# ARQUIVO: conexao.py
# OBJETIVO: Estabelecer a conexão com o banco de dados Supabase.
# =============================================================================

from supabase import create_client, Client

# Substitua pelas credenciais reais do seu painel do Supabase
SUPABASE_URL = "https://zhrrdztdczwzdahlzanp.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InpocnJkenRkY3p3emRhaGx6YW5wIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODc1OTEyNjYsImV4cCI6MjEwMzE2NzI2Nn0.i4m-nXRMFd46bFQKd6saTYiI12y5QBC4EVsLY08Kiqg"


def conectar_supabase() -> Client:
    """Inicializa e retorna o cliente de conexão com o Supabase."""
    try:
        cliente: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
        return cliente
    except Exception as e:
        print(f"❌ Erro ao conectar com o Supabase: {e}")
        return None

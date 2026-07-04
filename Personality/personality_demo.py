"""
Exemplo simplificado de Personalidade.
Mostra como aplicar diferentes estilos de resposta.
"""

from datetime import datetime

PERSONALIDADES = {
    "amigavel": {
        "erro": "Opa, algo deu errado, mas já estou verificando!"
    },
    "formal": {
        "erro": "Infelizmente ocorreu um erro. Por favor, tente novamente."
    },
    "entusiasta": {
        "erro": "Hmm, houve um problema técnico, mas vamos superar isso juntos!"
    }
}

PERSONALIDADE_ATUAL = "amigavel"

def aplicar_personalidade(resposta: str, tipo: str = None) -> str:
    perfil = PERSONALIDADES.get(tipo or PERSONALIDADE_ATUAL, PERSONALIDADES["amigavel"])
    return f"{resposta.strip()}"

def saudacao_inicial() -> str:
    hora = datetime.now().hour
    if hora < 12:
        saudacao = "Bom dia"
    elif hora < 18:
        saudacao = "Boa tarde"
    else:
        saudacao = "Boa noite"
    return aplicar_personalidade(f"{saudacao}! Sou sua assistente de modelagem 3D.")

def mensagem_erro(erro: str, tipo: str = None) -> str:
    perfil = PERSONALIDADES.get(tipo or PERSONALIDADE_ATUAL, PERSONALIDADES["amigavel"])
    return f"{perfil['erro']} Detalhes: {erro}"

# Exemplo de uso
if __name__ == "__main__":
    print(saudacao_inicial())
    print(aplicar_personalidade("Aqui está sua resposta!"))
    print(mensagem_erro("Falha na conexão", tipo="entusiasta"))

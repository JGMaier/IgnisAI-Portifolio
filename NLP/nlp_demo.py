"""
Exemplo simplificado de NLP (Natural Language Processing).
Mostra como o sistema recebe uma mensagem do usuário e gera uma resposta.
"""

class NLPDemo:
    def __init__(self):
        self.memory = []

    def gerar_resposta(self, user_message: str) -> str:
        """Gera uma resposta simples baseada na mensagem do usuário"""
        # Adiciona mensagem ao histórico
        self.memory.append(("user", user_message))

        # Aqui simulamos a resposta do modelo LLM
        resposta = f"Resposta gerada para: {user_message}"

        # Adiciona resposta ao histórico
        self.memory.append(("assistant", resposta))

        return resposta

    def get_history(self):
        """Retorna o histórico da conversa"""
        return self.memory

# Exemplo de uso
if __name__ == "__main__":
    nlp = NLPDemo()

    # Mensagem do usuário
    resposta1 = nlp.gerar_resposta("Olá, pode me ajudar?")
    print(resposta1)

    resposta2 = nlp.gerar_resposta("Quero aprender sobre modelagem 3D.")
    print(resposta2)

    # Histórico da conversa
    print("Histórico:", nlp.get_history())

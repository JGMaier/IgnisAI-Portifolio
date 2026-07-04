"""
Exemplo simplificado de Memória de Conversa.
Mostra como armazenar, recuperar e limpar histórico de mensagens.
"""

class ConversationMemory:
    def __init__(self):
        self.history = []

    def add_message(self, role: str, content: str):
        """Adiciona uma mensagem ao histórico"""
        self.history.append({"role": role, "content": content})

    def get_history(self):
        """Retorna todo o histórico"""
        return self.history

    def clear(self):
        """Limpa o histórico"""
        self.history = []

# Exemplo de uso
if __name__ == "__main__":
    memory = ConversationMemory()

    # Usuário envia mensagem
    memory.add_message("user", "Olá, pode me ajudar?")
    # Assistente responde
    memory.add_message("assistant", "Claro! O que você gostaria de saber?")

    print("Histórico atual:", memory.get_history())

    # Limpa histórico
    memory.clear()
    print("Histórico após limpar:", memory.get_history())

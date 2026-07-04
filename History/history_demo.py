"""
Exemplo simplificado de Histórico de Conversas.
Mostra como consultar e limpar o histórico.
"""

class ConversationMemoryDemo:
    def __init__(self):
        self.history = []

    def add_message(self, role: str, content: str):
        """Adiciona uma mensagem ao histórico"""
        self.history.append({"role": role, "content": content})

    def get_history(self, limit: int = None) -> dict:
        """Retorna o histórico completo ou limitado"""
        if limit is not None:
            return {"history": self.history[-limit:], "count": len(self.history[-limit:])}
        return {"history": self.history, "count": len(self.history)}

    def clear_history(self) -> dict:
        """Limpa todo o histórico"""
        self.history = []
        return {"message": "Histórico de conversas apagado com sucesso."}

# Exemplo de uso
if __name__ == "__main__":
    memory_demo = ConversationMemoryDemo()

    memory_demo.add_message("user", "Olá, IgnisAI!")
    memory_demo.add_message("assistant", "Olá! Como posso ajudar?")

    print("Histórico completo:", memory_demo.get_history())
    print("Última mensagem:", memory_demo.get_history(limit=1))

    print(memory_demo.clear_history())
    print("Histórico após limpar:", memory_demo.get_history())

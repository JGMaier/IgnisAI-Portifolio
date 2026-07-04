"""
Exemplo simplificado de Orquestrador.
Mostra apenas como o sistema decide se a mensagem do usuário é bate-papo
ou uma ação prática (como gerar um modelo 3D).
"""

class OrchestratorDemo:
    def __init__(self):
        self.memory = []

    def process_message(self, user_message: str) -> dict:
        """Decide se a mensagem é conversa ou ação prática"""
        mensagem_lower = user_message.lower()
        self.memory.append(("user", user_message))

        resposta = None
        action_type = "none"

        if "gerar modelo" in mensagem_lower or "criar 3d" in mensagem_lower:
            resposta = "Modelo 3D gerado com sucesso!"
            action_type = "ui_call"
        elif "rotacionar" in mensagem_lower:
            resposta = "Rotacionando objeto..."
            action_type = "ui_call"
        else:
            resposta = f"Resposta de bate-papo: {user_message}"
            action_type = "none"

        self.memory.append(("assistant", resposta))

        return {
            "response": resposta,
            "action": {"type": action_type}
        }

    def get_history(self):
        """Retorna o histórico da conversa"""
        return self.memory

# Exemplo de uso
if __name__ == "__main__":
    orchestrator = OrchestratorDemo()

    # Mensagem de bate-papo
    resultado1 = orchestrator.process_message("Olá, como você está?")
    print(resultado1)

    # Mensagem de ação prática
    resultado2 = orchestrator.process_message("Quero gerar modelo 3D")
    print(resultado2)

    # Histórico da conversa
    print("Histórico:", orchestrator.get_history())

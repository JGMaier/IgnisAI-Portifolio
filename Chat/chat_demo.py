"""
Exemplo simplificado de Chat Endpoint.
Mostra como o sistema recebe uma mensagem do usuário e retorna uma resposta.
"""

from datetime import datetime

class ChatDemo:
    def __init__(self):
        self.history = []

    def chat(self, user_message: str, user_id: str = "user123", session_id: str = "sess001", language: str = "pt") -> dict:
        """Simula o endpoint de chat"""
        print(f"[Chat] Mensagem recebida: {user_message}")
        self.history.append({"role": "user", "content": user_message})

        # Aqui simulamos o processamento da mensagem
        resposta = f"Resposta gerada para: {user_message}"
        self.history.append({"role": "assistant", "content": resposta})

        return {
            "ignisai_response": resposta,
            "history": self.history,
            "user_id": user_id,
            "session_id": session_id,
            "language": language,
            "timestamp": datetime.utcnow().isoformat()
        }

# Exemplo de uso
if __name__ == "__main__":
    chat_demo = ChatDemo()
    resultado = chat_demo.chat("Olá, IgnisAI!")
    print(resultado)

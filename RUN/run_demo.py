"""
Exemplo simplificado do módulo principal (run.py).
Mostra como iniciar a interface de chat da IgnisAI e integrar serviços básicos.
"""

class RunDemo:
    def __init__(self):
        self.chat_window = None
        self.tts_enabled = True
        self.nivel_ia = "rapida"
        self.voz_atual = "pf_dora"
        self.idioma_atual = "pt"

    def iniciar_chat(self):
        """Simula a abertura da janela de chat"""
        print("🔥 IgnisAI iniciada!")
        print("Mensagem de boas-vindas: Olá, sou sua assistente de modelagem 3D.")

    def enviar_mensagem(self, mensagem: str):
        """Simula envio de mensagem para a IA"""
        print(f"Usuário: {mensagem}")
        resposta = f"Resposta da IA para: {mensagem}"
        print(f"IgnisAI: {resposta}")
        return resposta

    def alterar_nivel_ia(self, nivel: str):
        """Troca o modelo de IA"""
        self.nivel_ia = nivel
        print(f"🤖 Inteligência ajustada para modo: {nivel.capitalize()}")

    def alterar_voz(self, voz: str):
        """Atualiza a voz do assistente"""
        self.voz_atual = voz
        print(f"🔊 Voz ajustada para: {voz} (Idioma atual: {self.idioma_atual})")

# Exemplo de uso
if __name__ == "__main__":
    demo = RunDemo()
    demo.iniciar_chat()
    demo.enviar_mensagem("Olá, IgnisAI!")
    demo.alterar_nivel_ia("detalhada")
    demo.alterar_voz("am_michael")

"""
Exemplo simplificado de integração com IgnisIA3D.
Mostra como verificar disponibilidade da API e gerar um modelo 3D.
"""

class IgnisIA3DClientDemo:
    def __init__(self, available=True):
        # Simula se a extensão IgnisIA3D está disponível
        self.available = available

    def is_available(self) -> bool:
        """Verifica se a API de geração 3D está disponível"""
        return self.available

    def gerar_modelo(self, caminho_imagem_guia: str, faces: int = 1000, steps: int = 50, device: str = "cpu") -> str:
        """Simula a geração de um modelo 3D"""
        if not caminho_imagem_guia:
            raise ValueError("Caminho da imagem guia não pode ser vazio.")

        if not self.is_available():
            raise RuntimeError("Serviço de geração desativado: Extensão 'IgnisIA3D' não encontrada.")

        # Simulação de geração
        print(f"[IgnisIA3D] Gerando modelo 3D com imagem {caminho_imagem_guia}, Faces={faces}, Steps={steps}, Device={device}")
        return "modelo_gerado.obj"

# Exemplo de uso
if __name__ == "__main__":
    client = IgnisIA3DClientDemo(available=True)

    if client.is_available():
        caminho_modelo = client.gerar_modelo("exemplo.png")
        print(f"Modelo 3D gerado em: {caminho_modelo}")
    else:
        print("Serviço IgnisIA3D não disponível.")

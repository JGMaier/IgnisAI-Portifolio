"""
Exemplo simplificado de Health Check.
Mostra como verificar o status da aplicação e informações básicas do sistema.
"""

import platform
import datetime

class HealthDemo:
    def health(self) -> dict:
        """Simula o endpoint de verificação de saúde"""
        try:
            system_info = {
                "api_name": "IgnisAI",
                "api_version": "1.0",
                "status": "IgnisAI está rodando!",
                "host": "localhost",
                "port": 8000,
                "system": platform.system(),
                "release": platform.release(),
                "python_version": platform.python_version(),
                "timestamp": datetime.datetime.utcnow().isoformat()
            }
            return system_info
        except Exception as e:
            return {"status": "Erro ao verificar saúde da aplicação", "error": str(e)}

# Exemplo de uso
if __name__ == "__main__":
    health_demo = HealthDemo()
    resultado = health_demo.health()
    print(resultado)

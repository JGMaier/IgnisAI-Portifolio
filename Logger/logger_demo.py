"""
Exemplo simplificado de Logger.
Mostra como configurar logs e obter um logger para diferentes módulos.
"""

import logging

# Configuração básica de logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[logging.StreamHandler()]
)

# Logger principal
logger = logging.getLogger("IgnisAI")

def get_logger(name: str):
    """Retorna um logger específico para um módulo"""
    return logging.getLogger(name)

# Exemplo de uso
if __name__ == "__main__":
    # Usando logger principal
    logger.info("Aplicação iniciada.")

    # Usando logger específico
    module_logger = get_logger("ModuloExemplo")
    module_logger.warning("Este é um aviso do módulo de exemplo.")

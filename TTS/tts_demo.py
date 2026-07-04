"""
Exemplo simplificado de uso do Kokoro-82M para TTS.
Mostra como carregar o modelo, configurar voz/idioma e sintetizar texto.
"""

import tempfile
from kokoro import KPipeline
import soundfile as sf

class TTSService:
    def __init__(self, model_name="hexgrad/Kokoro-82M", voice="pf_dora", language="pt", speed=1.0):
        self.model_name = model_name
        self.voice = voice
        self.language = language
        self.speed = speed
        self.pipeline = None
        self._init_pipeline()

    def _init_pipeline(self):
        """Carrega o pipeline Kokoro-82M"""
        self.pipeline = KPipeline(lang_code="p", repo_id=self.model_name)
        print(f"[TTS] Modelo {self.model_name} carregado com sucesso.")

    def synthesize(self, text: str) -> str:
        """Gera áudio a partir de texto e retorna caminho do arquivo WAV"""
        temp_audio = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
        output_path = temp_audio.name
        temp_audio.close()

        generator = self.pipeline(text, voice=self.voice, speed=self.speed)
        for _, _, audio in generator:
            sf.write(output_path, audio, 24000)
            break

        return output_path

# Exemplo de uso
if __name__ == "__main__":
    tts = TTSService()
    wav_path = tts.synthesize("Olá, este é um teste de síntese de voz.")
    print(f"Áudio gerado em: {wav_path}")

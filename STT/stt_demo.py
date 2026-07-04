"""
Exemplo simplificado de STT (Speech-to-Text) com Vosk.
Mostra como carregar o modelo, transcrever áudio e obter texto.
"""

import os
import wave
import json
from vosk import Model, KaldiRecognizer

class STTService:
    def __init__(self, model_path="models/vosk-model"):
        if not os.path.exists(model_path):
            print(f"[STT] Modelo Vosk não encontrado em {model_path}")
            self.model = None
            return

        self.model = Model(model_path)
        print(f"[STT] Modelo Vosk carregado com sucesso de [{model_path}]")

    def transcrever(self, arquivo_audio: str) -> str:
        """Transcreve áudio PCM 16-bit Mono em texto"""
        if not self.model:
            return "Erro: Modelo não inicializado."

        wf = wave.open(arquivo_audio, "rb")
        rec = KaldiRecognizer(self.model, wf.getframerate())

        while True:
            data = wf.readframes(4000)
            if len(data) == 0:
                break
            rec.AcceptWaveform(data)

        resultado = json.loads(rec.FinalResult())
        return resultado.get("text", "")

# Exemplo de uso
if __name__ == "__main__":
    stt = STTService()
    texto = stt.transcrever("exemplo.wav")  # arquivo de áudio gravado pelo usuário
    print(f"Texto reconhecido: {texto}")

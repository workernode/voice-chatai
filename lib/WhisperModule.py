import soundfile as sf
import numpy as np
from openai import OpenAI
from io import BytesIO
from typing import Optional

class WhisperModule:
    def __init__(self, location: str="local", api_key: Optional[str]=None) -> None:
        self.location = location
        self.api_key = api_key
        self.model = None
        self._initialize()

    def _initialize(self) -> None:
        if self.location == "local":
            import whisper
            # 読み込みの高速化
            model = whisper.load_model("large", device="cpu")
            _ = model.half()
            _ = model.cuda()
            for m in model.modules():
                if isinstance(m, whisper.model.LayerNorm):
                    m.float()

            self.model = model
            
        elif self.location == "api":
            client = OpenAI(api_key = self.api_key)
            model = client.audio.transcriptions
        
            self.model = model
    
    def transcribe(self, wav_stream: BytesIO) -> str:
        if self.location == "local":
            audio_array, sampling_rate = sf.read(wav_stream)
            audio_fp32 = audio_array.astype(np.float32)
            result = self.model.transcribe(
                audio_fp32, 
                verbose=True,
                language='japanese',
                beam_size=5,
                fp16=True,
                without_timestamps=True
            )
            text = result["text"]
            
        elif self.location == "api":
            wav_stream.name = 'from_mic.wav'
            text = self.model.create(model='whisper-1', file=wav_stream, response_format="text")

        return text

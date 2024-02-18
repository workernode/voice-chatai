import wave
import requests
import pyaudio
import io
import json
from time import sleep

class VoiceGenModule:
    def __init__(self, target_url: str):
        self.target_url = target_url

    def _post_audio_query(self, text: str) -> dict:
        params = {'text': text, 'speaker': 1} 
        audio_query = requests.post(self.target_url + "/audio_query", params=params)
        audio_query = audio_query.json()
        audio_query["speedScale"] = 1.2
        return audio_query

    def _post_synthesis(self, audio_query: dict) -> bytes:
        params = {'speaker': 1}
        headers = {'content-type': 'application/json'}
        query_json = json.dumps(audio_query)
        response = requests.post(
            self.target_url + "/synthesis",
            data=query_json,
            params=params,
            headers=headers
        )
        response = response.content
        return response

    def _play_sound(self, wav_file: bytes) -> None:
        wr: wave.Wave_read = wave.open(io.BytesIO(wav_file))
        audio = pyaudio.PyAudio()
        stream = audio.open(
            format=audio.get_format_from_width(wr.getsampwidth()),
            channels=wr.getnchannels(),
            rate=wr.getframerate(),
            output=True
        )
        chunk = 1024
        data = wr.readframes(chunk)
        while data:
            stream.write(data)
            data = wr.readframes(chunk)
        sleep(0.5)
        stream.close()
        audio.terminate()

    def text_to_voice(self, text: str) -> None:
        res = self._post_audio_query(text)
        wav = self._post_synthesis(res)
        self._play_sound(wav)


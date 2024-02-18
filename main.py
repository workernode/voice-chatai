from io import BytesIO
import speech_recognition as sr
import os

from lib.WhisperModule import WhisperModule
from lib.ChatModule import ChatModule
from lib.VoiceGenModule import VoiceGenModule

api_key = os.getenv("OPENAI_API_KEY")
target_url = os.getenv("VOICE_GEN_URL")

def main(location: str) -> None:
    model = WhisperModule(location=location, api_key=api_key)
    chatai = ChatModule(api_key)
    generater = VoiceGenModule(target_url)
    recognizer = sr.Recognizer()

    messages = chatai.initial_messege()

    while True:

        with sr.Microphone(sample_rate=16_000) as source:
            print("please speak")
            audio = recognizer.listen(source)

        print("processing ...")
    
        wav_stream = BytesIO(audio.get_wav_data())

        text = model.transcribe(wav_stream)

        print(text)

        messages.append(
            {'role': 'user', 'content': text}
        )

        response = chatai.chat(messages)

        print(response)

        generater.text_to_voice(response)

        messages.append(
            {'role': 'assistant', 'content': response}
        )

if __name__ == "__main__":
    main("api")
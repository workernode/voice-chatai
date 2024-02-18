from openai import OpenAI

class ChatModule:
    def __init__(self, api_key: str) -> None:
        self.client = OpenAI(api_key = api_key)

    def chat(self, messages: list) -> str:
        response = self.client.chat.completions.create(
            model='gpt-3.5-turbo',
            messages=messages
        )
        text = response.choices[0].message.content
        return text
    
    def initial_messege(self) -> list:
        messages = [
            {'role': 'system', 'content': 'あなたはずんだもんです。一人称は僕を使ってください。語尾に「なのだ」とつけてください'},
        ]
        return messages

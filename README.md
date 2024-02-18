## 1. はじめに

chatGPTと音声で会話できるようにするためのコード。


## 2. 前提

### 2.1. 共通

#### pyaudioのインストール

```shell
pip install pyaudio
```

pyaudioのインストールが失敗する場合はportaudioをインストールしてからpip installする


```shell
# Mac
brew install portaudio

# Ubuntu
apt-get install portaudio19-dev
```

#### speech recognitionのインストール

詳細は[こちら](https://github.com/Uberi/speech_recognition)を参照すること。
```shell
pip install git+https://github.com/Uberi/speech_recognition.git
```

#### openaiのインストール

openaiのpythonライブラリは1.12.0を利用すること。
```shell
pip install openai==1.12.0
```

#### VOICEVOXの準備

詳細は[こちら](https://github.com/VOICEVOX/voicevox_engine)を参照すること。
docker版を使ってもいいしGUI版を使ってもよい。

#### pulseaudioのインストール(docker利用時)

マイクをコンテナに認識させるためpulseaudioのインストールが必要になる。
```shell
apt-get install -y pulseaudio
```

### 2.2 WhisperをOpenAIのAPIで動かす場合

特にインストールするものはなし。

### 2.3 Whiperをlocalで動かす場合

#### Whisperのインストール

詳細は[こちら](https://github.com/openai/whisper)を参照すること。
```shell
pip install git+https://github.com/openai/whisper.git
```

## 3. 使い方

- 本レポジトリをローカルにcloneする。
- VOICEVOXを起動する。
- VOICEVOXのURLを環境変数`VOICE_GEN_URL`に登録する。

```shell
export VOICE_GEN_URL=127.0.0.1:50021
```
- OpenAIのAPIキーを環境変数`OPENAI_API_KEY`に登録する。

```shell
export OPENAI_API_KEY=xxxxxxxxxxxxxxxxxxxx
```
- Whisperをlocalで動かす場合は[`main.py`](main.py)の以下の部分を書き換える。

```python
# WhisperをOpenAIのAPIで動かす場合
if __name__ == "__main__":
    main("api")
```
```python
### Whiperをlocalで動かす場合
if __name__ == "__main__":
    main("local")

```
- [`main.py`](main.py)を起動する。
```shell
python main,py
```
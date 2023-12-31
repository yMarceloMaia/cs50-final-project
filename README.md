# Translator and Voice Cloner
## Video Demo: https://youtu.be/z_vU2fBJ_gs

## Description (ENGLISH):
Final project for Harvard's CS50 course, done in pairs by Yuzo Santana and Marcelo Maia.
This application was made in python and:
1. records the person's Portuguese speech
2. takes the recorded audio and transcribes its content using Google voice recognition
3. the transcribed text is then translated into English using Google's translator
4. the original speech audio is used as a sample in the Coqui-AI's text to speech local model XTTS-V2
5. an artificial speech is generated in English, copying the original voice

## BACKLOG (future implementations)
- make it work with any language

## How to install
First of all, make sure you are using Python 3.10.11 (exact version).

### Clone this repo
```git clone https://github.com/yMarceloMaia/cs50-final-project```

### Enter it's directory
```cd ./cs50-final-project```

### Create the .venv folder
```py -m venv .venv```

### Activate the virtual environment
```source .venv/Scripts/activate```

### Install the dependencies
```pip install -r requirements.txt```

### Make sure you have git-lfs installed
```git lfs install```

### Clone the local TTS model
```git clone https://huggingface.co/coqui/XTTS-v2```

### Run the app
```py src/app.py```

### Open your browser at localhost port 5000
http://localhost:5000

Click the record button and press SPACEBAR to start recording. Release the SPACEBAR to stop and wait for it to generate the voice. It might take a while depending on your hardware.

(PORTUGUÊS)
## Descrição:
Projeto final do curso CS50 da Harvard, feito em dupla por Yuzo e Marcelo.
Esse aplicativo foi feito em python e:
1. grava a fala em português da pessoa
2. pega o áudio gravado e transcreve seu conteúdo utilizando o reconhecimento de voz da Google
3. o texto transcrito é então traduzido para inglês utilizando o tradutor da Google
4. o áudio original da fala é utilizado como amostra no modelo texto para voz local XTTS-V2 da Coqui-AI
5. é gerada uma fala artificial em inglês, copiando a voz original

## Melhorias futuras
- gerar falas em qualquer língua

## Como instalar
Primeiramente, instale o Python 3.10.11 (versão exata).

### Clone este repo
```git clone https://github.com/yMarceloMaia/cs50-final-project```

### Entre na pasta
```cd ./cs50-final-project```

### Crie a pasta .venv
```py -m venv .venv```

### Ative o ambiente virtual
```source .venv/Scripts/activate```

### Instale as dependências
```pip install -r requirements.txt```

### Instale o git-lfs
```git lfs install```

### Clone o modelo TTS
```git clone https://huggingface.co/coqui/XTTS-v2```

### Rode o app
```py src/app.py```

### Abra seu navegador no localhost porta 5000
http://localhost:5000

Clique no botão de gravação e segure a barra de espaço enquanto fala. Solte a barra de espaço e aguarde a geração da voz. Pode levar um tempinho dependendo do seu hardware.
(RTX 4070 levou em média 35 segundos)

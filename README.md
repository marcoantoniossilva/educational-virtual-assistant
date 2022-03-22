# Assistente virtual educacional - Einstein

O Assistente virtual batizado de Einstein devolve para o usuário fórmulas matemáticas que lhes foi pedido, abaixo é possível acompanhar alguns exemplos de questionamentos a serem feitos ao Einstein:<br>

1 - Einstein, qual a fórmula da área de um quadrado?<br>
2 - Einstein, qual a fórmula do juros composto?<br>
3 - Einstein, qual a fórmula de bhaskara?<br>

Novas fórmulas podem ser inseridas no arquivo [data.json](data.json).<br>

<br>

## Tecnologias

O Assistente virtual educacional foi desenvolvido em [Python](https://www.python.org/) com o auxílio das bibliotecas: [nltk](https://www.nltk.org/) para processamento de linguagem natual, [pyaudio](https://pypi.org/project/PyAudio/) biblioteca de E/S de áudio multiplataforma utilizada pelo nltk, e por último a biblioteca [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) que é utilizada para reconhecimento de fala.<br>

<br>

## Vídeo explicativo

Para acessar o vídeo explicativo da ferramenta no Youtube, [clique aqui](https://youtu.be/5GaAR0DNdOc).

<br/>

## Requisitos

- [Python 3](https://www.python.org/downloads/)
- [nltk](https://www.nltk.org/)
- [pyaudio](https://pypi.org/project/PyAudio/)
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)

<br/>

## 1 - Instale o Python 3 e as bibliotecas:

O download do Python 3 pode ser feito [aqui](https://www.python.org/downloads/).<br>
Após a instalação do Python, abra o terminal na pasta do projeto e instale as bibliotecas com o seguinte comando:<br>

```bash
pip3 install -r requirements.txt
```

<br/>

## 2 - Execute o assistente:

Execute o arquivo [assistant.py](assistant.py) com o comando:

```bash
python3 assistant.py
```

<br/>

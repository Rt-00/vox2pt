# Audio Transcription & Translation Pipeline (PT-BR)

Pipeline local em Python para **transcrever áudio** e **traduzir o texto para português brasileiro (pt-BR)**, usando apenas ferramentas offline.

Sem APIs externas.  
Sem envio de dados para a nuvem.  
Reprodutível e extensível.

---

## Visão geral

Este projeto implementa a seguinte pipeline:

Áudio (mp3/wav/etc)  
→ Whisper (ASR)  
→ Texto no idioma original  
→ Argos Translate  
→ Texto traduzido para PT-BR  
→ Arquivo `.txt`

---

## Tecnologias utilizadas

- Python 3.11
- Whisper (speech-to-text)
- Argos Translate (machine translation offline)
- FFmpeg (processamento de áudio)

---

## Requisitos

### Sistema
- Linux, macOS ou Windows
- Python **3.11** ou **3.12** (não use Python 3.14)
- CPU (GPU é opcional)

### Dependência do sistema

O Whisper exige `ffmpeg` instalado:

**Linux**
```
sudo apt install ffmpeg
```

**macOS**
```
brew install ffmpeg
```

**Windows**
- Baixe do site oficial do FFmpeg
- Adicione ao PATH

---

## Instalação

### 1. Criar ambiente virtual

```
python3.11 -m venv venv
source venv/bin/activate
```

Verifique:
```
python --version
```

---

### 2. Instalar dependências

```
pip install --upgrade pip
pip install openai-whisper torch argostranslate
```

---

### 3. Instalar pacote de idioma (obrigatório)

O Argos **não baixa idiomas automaticamente**.  
Execute **uma única vez** para instalar `en → pt`:

```
python install_lang.py
```

---

## Uso

### Estrutura do projeto

```
.
├── main.py
├── audio.mp3
├── transcript_ptbr.txt
└── venv/
```

---

### Executar a pipeline

```
python main.py
```

Ao final, o arquivo `transcript_ptbr.txt` será criado com a transcrição traduzida para PT-BR.

---

## ⚠️ Avisos comuns

### FP16 warning
```
FP16 is not supported on CPU; using FP32 instead
```

Isso **não é erro**.

### Erro `NoneType has no attribute get_translation`
Indica que o pacote de idioma não foi instalado no Argos.

---

## 🚀 Possíveis evoluções

- Gerar legendas `.srt`
- Tradução por frases
- Processar uma pasta inteira
- Criar um CLI
- Adicionar timestamps
- Diarização de falantes

---# vox2pt

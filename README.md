# 📧 Classificação Automática de Emails

Este projeto é uma aplicação web simples que utiliza **Inteligência Artificial** para:
- Classificar emails em **Produtivo** ou **Improdutivo**.
- Sugerir respostas automáticas adequadas à categoria identificada (em Progresso e não finalizado).

O objetivo é **automatizar a leitura e resposta de emails**, liberando tempo da equipe e aumentando a produtividade.

---

## 🚀 Tecnologias Utilizadas
- **Python 3.10+**
- **Flask** (framework web)
- **Transformers (Hugging Face)** para NLP
- **PyPDF2** para leitura de PDFs
- **pysentimiento** para análise de sentimento em português/espanhol
- **HTML + CSS** para interface web

---

## 📂 Estrutura do Projeto

/Classificação de emails
│── backend/
│   ├── app.py               # Backend Flask
│   ├── classifier.py        # Classificação e geração de resposta
│   └── requirements.txt     # Dependências
│
│── frontend/
│   ├── index.html           # Interface principal
│   └── style.css            # Estilo visual
│
│── README.md                # Instruções do projeto

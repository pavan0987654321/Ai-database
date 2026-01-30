🚀 AskDB AI — Natural Language SQL Retail Assistant

AskDB AI is an AI-powered database question-answering application that converts natural language questions into SQL queries, executes them on a retail database, and returns clean, human-readable answers.

The system combines LangChain, LLMs, vector similarity search, and MySQL to enable business-style Q&A over structured data — without writing SQL manually.

🎯 Features

✅ Ask questions in plain English

✅ Automatic Natural Language → SQL conversion

✅ Executes queries on MySQL retail database

✅ Returns formatted business-friendly answers

✅ Few-shot prompt learning for better SQL accuracy

✅ Vector similarity example selection (FAISS)

✅ Streamlit web interface

✅ Secure environment variable based API keys

✅ OpenRouter / LLM compatible backend

🧠 Example Questions

You can ask:

How many white Nike t-shirts are in stock?

Show stock available by size for Adidas black shirts

What is the total inventory for Puma products?

Which size has the highest stock?

Give me discount details for shirt ID 10

🏗️ Tech Stack

Python

LangChain

LLM via OpenRouter

FAISS Vector Store

HuggingFace Embeddings

MySQL

Streamlit

SQLAlchemy

📂 Project Structure
AskDB-AI/
│
├── database/
│   ├── db_creation_atliq_t_shirts.sql
│   └── db_setup.sql
│
├── few_shots.py
├── langchain_helper.py
├── main.py
├── requirements.txt
├── .env              # (not committed)
├── .gitignore
└── README.md

⚙️ Setup Instructions
1️⃣ Clone Repository
git clone https://github.com/YOUR_USERNAME/AskDB-AI.git
cd AskDB-AI

2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Setup Environment Variables

Create a .env file:

OPENROUTER_API_KEY=your_api_key_here
DB_USER=root
DB_PASSWORD=your_password
DB_HOST=localhost
DB_NAME=atliq_tshirts


⚠️ Never commit .env to GitHub.

5️⃣ Setup Database

Open MySQL Workbench and run:

database/db_creation_atliq_t_shirts.sql


This will create tables and sample data.

▶️ Run Application
streamlit run main.py


Open browser:

http://localhost:8501

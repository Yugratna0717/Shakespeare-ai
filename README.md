# 🎭 Shakespeare AI

An AI-powered Shakespeare tutor built with **Streamlit** and **Google Gemini** that explains Shakespearean plays in simple modern English.

Users can enter a play name, act number, and scene number, and the AI generates line-by-line explanations in easy-to-understand language.

---

## ✨ Features

- 📖 Explain Shakespeare scenes line by line
- 🗣️ Convert Elizabethan English into modern English
- 🌐 Interactive web interface built with Streamlit
- 🤖 Powered by Google's Gemini API
- ⚡ Fast and lightweight deployment using Streamlit Community Cloud

---

## 🛠️ Tech Stack

| Package | Purpose |
|---------|---------|
| `streamlit` | Builds the interactive web application |
| `google-generativeai` | Connects the app to Google's Gemini models |
| `python-dotenv` | Loads API keys from a `.env` file |
| `os` | Accesses environment variables |

---

## 📂 Project Structure

```text
Shakespeare-ai/

├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── .env
└── venv/
```

---

## 🚀 Installation

### Clone the repository

```bash
git clone https://github.com/Yugratna0717/Shakespeare-ai.git

cd Shakespeare-ai
```

### Create a virtual environment

#### macOS / Linux

```bash
python3 -m venv venv

source venv/bin/activate
```

#### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project directory.

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

Replace `YOUR_GEMINI_API_KEY` with your actual Gemini API key.

---

## ▶️ Running the Application

Run the Streamlit app:

```bash
streamlit run app.py
```

The application will open in your browser at:

```text
http://localhost:8501
```

---

## 📦 Requirements

```txt
streamlit
google-generativeai
python-dotenv
```

---

## 🎯 Future Improvements

- 📚 Scene summaries
- 👤 Character analysis
- ⭐ Important quotes
- 📝 Exam-style questions
- 🎨 Improved UI/UX
- 📖 Support for additional literary works

---

## 👨‍💻 Author

**Yugratna**

Built using **Python**, **Streamlit**, and **Google Gemini**.

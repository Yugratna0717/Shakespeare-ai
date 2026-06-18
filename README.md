# 🎭 Shakespeare AI
 
> An AI-powered web application that explains Shakespeare plays scene by scene in simple, modern English — powered by Google Gemini 2.5 Flash and Streamlit.
 
---
 
## 📸 Preview
 
![Shakespeare AI](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Google Gemini](https://img.shields.io/badge/Google%20Gemini-8E75B2?style=for-the-badge&logo=google&logoColor=white)
 
---
 
## ✨ Features
 
- 📖 Enter any Shakespeare play, act, and scene
- 🧠 Get line-by-line explanations in simple modern English
- 💬 Original dialogue preserved with speaker names
- 🔍 Difficult words, metaphors, and references explained
- ⚡ Powered by Google Gemini 2.5 Flash
---
 
## 🛠️ Tech Stack
 
| Technology | Purpose |
|------------|---------|
| Python | Core language |
| Streamlit | Web interface |
| Google Gemini 2.5 Flash | AI explanations |
| python-dotenv | Environment variable management |
 
---
 
## 🚀 Getting Started
 
### Prerequisites
- Python 3.8+
- A [Google Gemini API Key](https://aistudio.google.com/app/apikey)
### Installation
 
1. **Clone the repository**
```bash
   git clone https://github.com/Yugratna0717/shakespeare-ai.git
   cd shakespeare-ai
```
 
2. **Create and activate a virtual environment**
```bash
   python -m venv venv
   source venv/bin/activate        # Mac/Linux
   venv\Scripts\activate           # Windows
```
 
3. **Install dependencies**
```bash
   pip install -r requirements.txt
```
 
4. **Set up your API key**
   Create a `.env` file in the project root:
```
   GEMINI_API_KEY=your_actual_api_key_here
```
 
5. **Run the app**
```bash
   streamlit run app.py
```
 
   The app will open at `http://localhost:8501`
 
---
 
## 📁 Project Structure
 
```
shakespeare-ai/
├── app.py              # Main Streamlit application
├── test.py             # API connection test script
├── requirements.txt    # Python dependencies
├── .env                # API key (not pushed to GitHub)
├── .gitignore          # Git ignore rules
└── README.md           # Project documentation
```
 
---
 
## 🔐 Environment Variables
 
| Variable | Description |
|----------|-------------|
| `GEMINI_API_KEY` | Your Google Gemini API key from [Google AI Studio](https://aistudio.google.com/) |
 
> ⚠️ Never push your `.env` file to GitHub. It is already included in `.gitignore`.
 
---
 
## 🧪 Testing
 
To verify your API connection is working:
```bash
python test.py
```
 
---
 
## 🌐 Deployment
 
This app can be deployed for free on [Streamlit Cloud](https://share.streamlit.io):
 
1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io) and connect your repo
3. Set `app.py` as the main file
4. Add your `GEMINI_API_KEY` under **Settings → Secrets**
5. Click **Deploy**
---
 
## 👩‍💻 Author
 
**Yugratna**
- GitHub: [@Yugratna0717](https://github.com/Yugratna0717)
---
 

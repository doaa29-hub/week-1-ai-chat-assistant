# AI Chat Assistant

## Project Description
A conversational AI chat assistant built in Python using the Groq API (Llama 3.3 70B model). The assistant maintains conversation memory within a session and is available in two forms: a command-line interface (CLI) and a web-based interface built with Streamlit. This project was built as the first task of the AI Internship Program.

## Features
- Real-time responses powered by a large language model (Llama 3.3 70B via Groq)
- Conversation memory — the assistant remembers earlier messages within the same session
- Two interfaces: terminal-based CLI and browser-based Streamlit web app
- Error handling for failed or interrupted API calls
- Clear chat option (web UI)
- API key stored securely using environment variables, never hardcoded

## Technologies Used
- Python 3.12
- [Groq API](https://console.groq.com) (Llama 3.3 70B Versatile model)
- Streamlit (web interface)
- python-dotenv (environment variable management)

## Installation Instructions

1. Clone this repository:
   ```bash
   git clone https://github.com/doaa29-hub/ai-chat-assistant.git
   cd ai-chat-assistant
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # Mac/Linux
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Setup Instructions

1. Get a free API key from [Groq Console](https://console.groq.com/keys).
2. Copy `.env.example` to a new file named `.env`.
3. Open `.env` and paste your real API key:
   ```
   GROQ_API_KEY=your_actual_key_here
   ```

## Usage Guide

### Run the CLI version:
```bash
python main.py
```
Type your message and press Enter. Type `exit` or `quit` to end the session.

### Run the web interface:
```bash
streamlit run app.py
```
This opens a browser tab with a chat interface. Type your message in the input box at the bottom.

### Test your API connection:
```bash
python test.py
```
Use this to confirm your API key and setup work before running the full assistant.

## Project Structure
```
ai-chat-assistant/
│
├── main.py              # CLI chat assistant with conversation memory
├── app.py                # Streamlit web interface
├── test.py               # Minimal script to test API connection
├── requirements.txt      # Python dependencies
├── .env.example           # Sample environment variable file
├── .gitignore             # Files excluded from version control
└── README.md              # Project documentation
```

## Example Output

**CLI:**
```
AI Chat Assistant (type 'exit' or 'quit' to leave)

You: What is Python?
Assistant: Python is a high-level, interpreted programming language known for its readability and versatility...

You: exit
Goodbye!
```

**Web Interface:** Chat bubbles displayed in a browser, with a sidebar option to clear the conversation.

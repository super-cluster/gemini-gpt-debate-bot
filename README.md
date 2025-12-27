# Self-Talking Chatbot

A Python application that simulates an AI debate between two language models (Gemini and Ollama) on the topic of solo travel. The chatbot creates a self-sustaining conversation where each model responds to the other's arguments, forming a competitive debate.

## Features

- **Dual AI Models**: Uses Google's Gemini and Ollama models for debate simulation
- **Real-time Streaming**: Displays responses as they're generated using IPython's display features
- **Debate Simulation**: Models take opposing sides on solo travel (Gemini: against, Ollama: in support)
- **Multiple Rounds**: Runs 10 rounds of back-and-forth debate arguments
- **Markdown Display**: Beautiful markdown rendering for easy reading

## Requirements

- Python >= 3.12
- API keys for:
  - Google Gemini API
  - Ollama API

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd self-talking-chatbot
```

2. Install dependencies using `uv`:
```bash
uv sync
```

Or using pip:
```bash
pip install -r requirements.txt
```

## Configuration

1. Create a `.env` file in the project root:
```env
GEMINI_API_KEY=your_gemini_api_key_here
OLLAMA_API_KEY=your_ollama_api_key_here
```

2. Make sure your API keys are properly set up:
   - **Gemini API Key**: Get it from [Google AI Studio](https://makersuite.google.com/app/apikey)
   - **OLLAMA_API_KEY**: Required for Ollama API access

## Usage

Run the script:
```bash
python main.py
```

**Note**: This script uses IPython's display features (`display`, `update_display`), which work best in Jupyter notebooks. For best experience, consider running it in a Jupyter notebook environment.

The script will:
1. Display the initial arguments from both models
2. Run 10 rounds of debate
3. Stream and display each response in real-time using markdown formatting

## Project Structure

```
self-talking-chatbot/
├── main.py              # Main application code
├── requirements.txt     # Python dependencies
├── pyproject.toml      # Project configuration
├── .env                # Environment variables (create this)
└── README.md           # This file
```

## How It Works

1. **Initial Setup**: Two initial arguments are set:
   - Gemini: "Solo travel sucks."
   - Ollama: "Solo Travel is best way to explore yourself."

2. **Debate Loop**: For 10 rounds:
   - Gemini receives all previous arguments and responds (arguing against solo travel)
   - Ollama receives all previous arguments and responds (arguing in support of solo travel)
   - Each response is added to the conversation history

3. **Real-time Display**: Responses are streamed and displayed using IPython's markdown rendering, updating in real-time as text is generated.

## Models Used

- **Gemini**: `gemini-2.5-flash-lite` (argues against solo travel)
- **Ollama**: `gpt-oss:120b` (argues in support of solo travel)

## Dependencies

- `openai` - OpenAI-compatible API client
- `python-dotenv` - Environment variable management
- `ipython` - IPython display features
- `ipykernel` - Jupyter kernel support
- `ipywidgets` - Interactive widgets



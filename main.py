import os
from turtle import mode
from openai import OpenAI
from dotenv import load_dotenv
from IPython.display import Markdown, display, update_display

load_dotenv(override=True)

gemini_api_key = os.getenv('GEMINI_API_KEY')
ollama_api_key = os.getenv('OLLAMA_API_KEY')
gemini_url = "https://generativelanguage.googleapis.com/v1beta/openai/"
ollama_url = "https://ollama.com/v1"

if gemini_api_key:
    print("Gemini API key loaded")
else:
    print("Gemini API key not found")
if ollama_api_key:
    print("Ollama API key loaded")
else:
    print("Ollama API key not found")

gemini_client = OpenAI(base_url=gemini_url, api_key=gemini_api_key)
ollama_client = OpenAI(base_url=ollama_url, api_key=ollama_api_key)

gemini_system_prompt = "You are a competetive candidate whose goal is to win a debate. You are always on the against side of the topic. You try to find loophole in other candidate argument and defend your position. The topic of debate is Solo travel. Answer as short as possible."
ollama_system_prompt = "You are a competetive candidate whose goal is to win a debate. You are always on the support side of the topic. You try to find loophole in other candidate argument and defend your position. The topic of debate is Solo travel. Answer as short as possible"

gemini_argument = ["Solo travel sucks."]
ollama_argument = ["Solo Travel is best way to expolre yourself."]

def call_gemini():
    messages = [{"role": "system", "content": gemini_system_prompt}]
    for gemini, ollama in zip(gemini_argument, ollama_argument):
        messages.append({"role":"assistant", "content":gemini})
        messages.append({"role":"user", "content": ollama})
    stream = gemini_client.chat.completions.create(model="gemini-2.5-flash-lite", messages=messages, stream=True);
    display(Markdown(f"### Gemini:\n"))
    display_handle = display(Markdown(""), display_id=True);
    response = "";
    for chunk in stream:
        response += chunk.choices[0].delta.content or ''
        update_display(Markdown(response), display_id=display_handle.display_id)
    return response;

def call_ollama():
    messages = [{"role": "system", "content": ollama_system_prompt}]
    for gemini, ollama in zip(gemini_argument, ollama_argument):
        messages.append({"role":"user", "content":gemini})
        messages.append({"role":"assistant", "content": ollama})
    messages.append({"role":"user", "content":gemini_argument[-1]})
    stream = ollama_client.chat.completions.create(model="gpt-oss:120b", messages=messages, stream=True);
    display(Markdown(f"### Ollama:\n"))
    display_handle = display(Markdown(""), display_id=True);
    response = "";
    for chunk in stream:
        response += chunk.choices[0].delta.content or ''
        update_display(Markdown(response), display_id=display_handle.display_id)
    return response;

def main():
    display(Markdown(f"### Gemini:\n{gemini_argument[0]}\n"))
    display(Markdown(f"### Ollama:\n{ollama_argument[0]}\n"))

    for i in range(10):
        gemini_next = call_gemini()
        gemini_argument.append(gemini_next)

        ollama_next = call_ollama()
        ollama_argument.append(ollama_next)


if __name__ == "__main__":
    main()

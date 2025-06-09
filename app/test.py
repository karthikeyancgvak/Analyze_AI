# app/test.py
import ollama

def greet(name):
    prompt = f"Generate a creative greeting for someone named {name}."
    
    # Use Ollama to generate a response
    response = ollama.chat(
        model='deepseek-r1:1.5b',
        messages=[{"role": "user", "content": prompt}]
    )
    
    return response['message']['content']

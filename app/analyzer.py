# app/analyzer.py

import ollama

def analyze_text_file(content):
    prompt = (
        "You are an expert data and content analyst.\n"
        "Given the following file content, summarize and provide insights such as patterns, key information, anomalies, or trends.\n\n"
        f"{content}\n\n"
        "Return a well-structured, easy-to-read summary."
    )

    try:
        response = ollama.chat(
            model='deepseek-r1:1.5b',
            messages=[{"role": "user", "content": prompt}]
        )
        return response['message']['content']
    except Exception as e:
        return f"❌ Error: {str(e)}"

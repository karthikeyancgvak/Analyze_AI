# main.py

import streamlit as st
from app.analyzer import analyze_text_file

def main():
    st.title("📄 AI File Analyzer")
    st.write("Upload a text file to get insights powered by Ollama (deepseek-r1:1.5b).")

    uploaded_file = st.file_uploader("Choose a file", type=["txt", "csv", "md", "log"])

    if uploaded_file is not None:
        content = uploaded_file.read().decode("utf-8")

        if st.button("Analyze with AI"):
            with st.spinner("Analyzing..."):
                result = analyze_text_file(content)
                st.subheader("🔍 Insights from AI:")
                st.write(result)

if __name__ == "__main__":
    main()

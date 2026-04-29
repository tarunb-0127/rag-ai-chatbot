
# RAG AI Chatbot - Pizza Restaurant Q&A Bot
<img width="700" height="500" alt="image" src="https://github.com/user-attachments/assets/6b0821ef-51ef-45e5-8322-1c2463e56ff2" />
This project is an interactive chatbot built with **LangChain**, **Ollama**, and **Chroma**. It uses Retrieval‑Augmented Generation (RAG) to answer user questions about a pizza restaurant by retrieving relevant customer reviews from a vector database and generating responses with a local LLM.

Features
--------
- Interactive command‑line chatbot with rich formatting and spinner animations.
- Retrieval‑Augmented Generation (RAG): pulls relevant reviews before answering.
- Chroma vector store for fast semantic search.
- Ollama LLM for natural language responses.
- Uses `.env` file to store configuration (Ollama server URL).
- Customizable spinner styles (for example, “nom nom”).

Requirements
------------
- Python 3.9+
- Ollama running locally or in Docker.
- Dependencies:
   ```bash
   pip install -r requirements.txt
   ```

Setup
-----
1. Clone the repository.
2. Create a `.env` file in the project root:
   ```
   OLLAMA_BASE_URL=http://localhost:11434
   ```
3. Run Ollama in Docker:
   ```bash
   docker run -d --name myllama -p 11434:11434 ollama/ollama
   docker exec -it myllama ollama pull llama3
   ```
4. Prepare the vector store:
   - On first run, reviews from `realistic_restaurant_reviews.csv` will be embedded and stored in Chroma.
5. Start the chatbot:
   ```bash
   python main.py
   ```

Usage
-----
- Type your questions in the terminal (for example, `Tell me about the ambience`).
- The chatbot retrieves relevant reviews and responds using the LLaMA model.
- Type `q`, `quit`, or `exit` to quit.

Example
-------
```
RAG AI Chatbot - Pizza Restaurant Q&A Bot
Type your question, or 'q' to quit.

Ask a question: Tell me about the ambience
Relevant Reviews:
[2024-01-30] ⭐ 3 - Too noisy for conversation...
[2024-01-20] ⭐ 1 - Dirty restaurant...

Answer:
The ambience is often described as noisy and not ideal for conversation, with some concerns about cleanliness.
```

Notes
-----
- The folder `chroma_langchain_db/` is ignored in Git via `.gitignore` to avoid tracking local database files.
- The conversation history is stored in memory during runtime.
- Update `.env` if your Ollama server runs on a different host or port.
- You can change the spinner style in `main.py` (for example, `"nom"`).


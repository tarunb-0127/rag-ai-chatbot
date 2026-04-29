from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from halo import Halo
from vector import retriever


load_dotenv()
console = Console()

model = OllamaLLM(model="llama3", base_url=os.getenv("OLLAMA_BASE_URL"))


template = """
You are an expert in answering questions about a pizza restaurant.

Here are some relevant reviews: {reviews}

Here are some questions to answer: {question}
"""
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def format_reviews(reviews):
    """Convert list of Document objects into readable text."""
    if not reviews:
        return "No reviews found."
    formatted = []
    for doc in reviews:
        rating = doc.metadata.get("rating", "N/A")
        date = doc.metadata.get("date", "Unknown date")
        content = doc.page_content
        formatted.append(f"[{date}] ⭐ {rating} - {content}")
    return "\n\n".join(formatted)

def main():
    console.print("[bold green]🍕 Pizza Restaurant Q&A CLI[/bold green]")
    console.print("Type your question, or 'q' to quit.\n")

    while True:

        question = Prompt.ask("[bold cyan]Ask a question[/bold cyan]")
        if question.lower() in ["q", "quit", "exit"]:
            console.print("\n[bold red]Goodbye![/bold red]")
            break

  
        reviews = retriever.invoke(question)
        reviews_text = format_reviews(reviews)
        console.print(Panel(reviews_text, title="Relevant Reviews", expand=False))

  
        spinner = Halo(text="Thinking...", spinner="nom")
        spinner.start()
        result = chain.invoke({"reviews": reviews_text, "question": question})
        spinner.stop()


        console.print(Panel(result, title="Answer", style="bold green"))

if __name__ == "__main__":
    main()

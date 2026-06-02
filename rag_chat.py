from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
import ollama

DB_PATH = "vectorstore"
MODEL_NAME = "qwen3.6"

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

db = FAISS.load_local(
    DB_PATH,
    embeddings,
    allow_dangerous_deserialization=True
)

def ask_question(question: str) -> str:
    docs = db.similarity_search(question, k=3)

    context = "\n\n".join([doc.page_content for doc in docs])

    prompt = f"""
You are an enterprise AI assistant.
Answer only using the context below.
If the answer is not in the context, say: "I don't know based on the provided documents."

Context:
{context}

Question:
{question}

Answer:
"""

    response = ollama.chat(
        model=MODEL_NAME,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response["message"]["content"]


if __name__ == "__main__":
    while True:
        q = input("\nAsk: ")
        if q.lower() in ["exit", "quit"]:
            break
        print("\nAnswer:", ask_question(q))
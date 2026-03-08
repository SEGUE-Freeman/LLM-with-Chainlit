from langchain_ollama import ChatOllama
from src.prompt import system_instruction

# On initialise Llama 3 localement
client = ChatOllama(model="llama3.2:1b", temperature=0)

# Initialisation de l'historique avec l'instruction système
messages = [
    {"role": "system", "content": system_instruction}
]

def ask_order(messages):
    # .invoke est l'équivalent de client.chat.completions.create
    response = client.invoke(messages)
    return response.content
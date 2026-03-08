import chainlit as cl
from src.llm import ask_order

@cl.on_chat_start
async def start():
    # On initialise l'historique dans la session propre à l'utilisateur
    from src.prompt import system_instruction
    cl.user_session.set("messages", [{"role": "system", "content": system_instruction}])
    await cl.Message(content="Assistant Syfl Data prêt ! Comment puis-je t'aider aujourd'hui ?").send()

@cl.on_message
async def main(message: cl.Message):
    # Récupérer l'historique stocké
    history = cl.user_session.get("messages")
    history.append({"role": "user", "content": message.content})
    
    # Afficher un indicateur de chargement
    msg = cl.Message(content="")
    await msg.send()

    # Appel asynchrone pour éviter que l'interface ne gèle
    # Avec Llama 3.2 1B, ce sera très rapide !
    response = await cl.make_async(ask_order)(history)
    
    history.append({"role": "assistant", "content": response})
    cl.user_session.set("messages", history)
    
    # Mise à jour du message avec la réponse
    msg.content = response
    await msg.update()
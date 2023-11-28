import base64
from typing import List

import openai
import requests

# Assumi che queste siano le tue chiavi API personali di OpenAI
api_key = ''


# Inizializza la storia della conversazione
conversation_history = []


def get_text_to_chat(
        message: str,
        conversation_history: List[str],
        role: str = "user",
        max_tokens: int = 1024,
        model: str = "gpt-4-vision-preview"
):
    conversation_history.append(f"User: {message}")
    context = "\n".join(conversation_history)
    headers = {
        "Content-Type":  "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    # content_list = []
    # text_part = {"type": "text", "text": message_text}
    # content_list.append(text_part)
    payload = {
        "model":      model,
        "messages":   [
            {
                "role":    role,
                "content": context
            }
        ],
        "max_tokens": max_tokens,
    }
    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload).json()
    message_response = response.get('choices')[0].get('message').get('content')
    conversation_history.append(f"GPT-4: {message_response}")
    return message_response, conversation_history


def image_input_to_chat(message_text: str,
                        base_img: List or base64,
                        file_ext: str = None,
                        role: str = "user",
                        max_tokens: int = 1024,
                        model: str = "gpt-4-vision-preview"):
    global conversation_history  # Utilizza la variabile globale per mantenere lo stato

    # Aggiungi il nuovo prompt alla storia della conversazione
    conversation_history.append(f"User: {message_text}")

    headers = {
        "Content-Type":  "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    content_list = []
    text_part = {"type": "text", "text": message_text}
    content_list.append(text_part)
    if isinstance(base_img, list):
        for el in base_img:
            img_part = {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{el}"}}
            content_list.append(img_part)
    else:
        img_part = {"type": "image_url", "image_url": {"url": f"data:image/{file_ext};base64,{base_img}"}}
        content_list.append(img_part)

    payload = {
        "model":      model,
        "messages":   [
            {
                "role":    role,
                "content": content_list
            }
        ],
        "max_tokens": max_tokens,
    }
    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload).json()
    message_response = response.get('choices')[0].get('message').get('content')

    # Aggiungi la risposta del modello alla storia della conversazione
    conversation_history.append(f"GPT-4: {message_response}")
    return message_response


def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


if __name__ == '__main__':
    # Esempio di utilizzo
    message_text = "Descrivi questa immagine"
    image_path = "../../Resources/coperta-gatto-divano-ferplast.jpg"
    base64_image = encode_image(image_path)
    file_ext = "jpg"  # Sostituisci con il formato corretto dell'immagine

    first_message = image_input_to_chat(message_text=message_text,
                                        base_img=base64_image,
                                        file_ext=file_ext)

    second_message, conversation_history = get_text_to_chat(
        message="In base all'immagine analizzata in precedenza, di che colore è il gatto?",
        conversation_history=conversation_history
    )
    third_message, conversation_history = get_text_to_chat(
        message="In base all'immagine analizzata in precedenza, di che colore è il divano?",
        conversation_history=conversation_history
    )

    print(first_message)
    print("-" * 150)
    print(second_message)
    print("-" * 150)
    print(first_message)

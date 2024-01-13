import requests
import json
import gradio as gr

url = "http://localhost:11434/api/generate"

headers = {
    'Content-Type': 'application/json'
}

# Conversation history
conversation_history = []

def generate_response(prompt):

    conversation_history.append(prompt)
    full_prompt = "\n".join(conversation_history)
    
    data = {
        "model" : "mistral",
        "stream" : False,
        "prompt" : full_prompt
    }
    
    response = requests.post(url,headers=headers,data=json.dumps(data))

    if response.status_code == 200 :
        response_text = response.text
        data = json.loads(response_text)
        result = data["response"]
        conversation_history.append(result)
        return result
    else:
        print("Error :", response.status_code, response.text)
        return None

interface = gr.Interface(fn=generate_response,inputs="text",outputs="text")

interface.launch()
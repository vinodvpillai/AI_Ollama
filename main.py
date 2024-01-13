import requests
import json
import gradio as gr

url = "http://localhost:11434/api/generate"

headers = {
    'Content-Type': 'application/json'
}

def generate_response(prompt):
    
    data = {
        "model" : "mistral",
        "stream" : False,
        "prompt" : prompt
    }
    
    response = requests.post(url,headers=headers,data=json.dumps(data))

    if response.status_code == 200 :
        response_text = response.text
        data = json.loads(response_text)
        return data["response"]
    else:
        print("Error :", response.status_code, response.text)
        return None

interface = gr.Interface(fn=generate_response,inputs="text",outputs="text")

interface.launch()
from fastapi import FastAPI
import requests
import uvicorn

app = FastAPI()

API_URL = "https://api-inference.huggingface.co/models/meta-llama/Meta-Llama-3-8B-Instruct"
HUGGING_FACE_TOKEN = "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"

@app.get("/")
def read_root():
    headers = {
        "Authorization": f"Bearer {HUGGING_FACE_TOKEN}"
    }
    
    data = {
        "inputs": "Tell me more about Carnegie Mellon University in Qatar"
    }

    response = requests.post(API_URL, headers=headers, json=data)
    new = response.json()[0]['generated_text'].split('\n')
    return new

if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000)
import requests

OPENAI_API_URL = "https://api.openai.com/v1/engines/davinci/completions" # This URL might change based on the OpenAI version you're using.
OPENAI_API_KEY = "YOUR_OPENAI_API_KEY"

@app.route('/ask', methods=['POST'])
def ask_openai():
    question = request.json.get('question')
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "prompt": question,
        "max_tokens": 150
    }
    response = requests.post(OPENAI_API_URL, headers=headers, json=payload)
    answer = response.json().get('choices')[0].get('text').strip()
    return jsonify({"answer": answer})

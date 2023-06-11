from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

@app.route('/api/generate-story', methods=['POST'])
def generate_story():
    data = request.json
    prompt = 'Story Type: ' + data['story_type'] + '\nStory Style: ' + data['story_style'] + '\nCharacter: ' + data['character_description'] + '\nKeywords: ' + data['keywords'] + '\n\nOnce upon a time, '

    response = requests.post('https://api.openai.com/v1/engines/davinci-codex/completions', headers={
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {os.getenv("OPENAI_KEY")}'
    }, json={
        'prompt': prompt,
        'max_tokens': 100
    })

    return jsonify(response.json()), 200

if __name__ == "__main__":
    app.run(port=5000, debug=True)
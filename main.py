import os
from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)
openai.api_key = "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"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ai_help", methods=["POST"])
def ai_help():
    prompt = request.json.get("prompt", "")
    resp = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role":"system","content":"तुम helpful कोडिंग असिस्टेंट हो"},
            {"role":"user","content":prompt}
        ]
    )
    return jsonify({"code_suggestion": resp.choices[0].message.content})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 3000)))

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def get_bot_response(message):
    message = message.lower()
    if "merhaba" in message:
        return "Merhaba! Sana nasıl yardımcı olabilirim?"
    elif "nasılsın" in message:
        return "İyiyim, sen nasılsın?"
    elif "görüşürüz" in message:
        return "Görüşmek üzere!"
    else:
        return "Üzgünüm bunu anlayamadım."

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chatbot_response():
    user_message = request.json.get("message")
    response = get_bot_response(user_message)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
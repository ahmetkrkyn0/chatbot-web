from flask import Flask, render_template, request, jsonify
import requests

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

OMDB_API_KEY = "5d7d7304"

def omdb_film_oner(tur="action"):
    url = f"http://www.omdbapi.com/?apikey={OMDB_API_KEY}&type=movie&s={tur}"
    response = requests.get(url)
    data = response.json()

    if data.get("Response") == "True":
        filmler = [film["Title"] for film in data["Search"]]
        return filmler
    else:
        return "Üzgünüm, şu anda öneri veremiyorum. Türü doğru girdiğinizden emin misin?"



@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def get_bot_response():
    userText = request.form["msg"].lower()

    for tur in ["action", "comedy", "horror", "romance", "drama", "sci-fi"]:
        if tur in userText:
            return omdb_film_oner(tur)

    return "Hangi türde film istediğini belirtir misin? (örneğin: action, comedy)"


if __name__ == "__main__":
    app.run(debug=True)
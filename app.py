from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

OMDB_API_KEY = "5d7d7304"

tur_map = {
    "aksiyon": "action",
    "komedi": "comedy",
    "korku": "horror",
    "romantik": "romance",
    "dram": "drama",
    "bilim kurgu": "sci-fi",
    "action": "action",
    "comedy": "comedy",
    "horror": "horror",
    "romance": "romance",
    "drama": "drama",
    "sci-fi": "sci-fi"
}

def get_tur_from_message(msg):
    for key in tur_map:
        if key in msg:
            return tur_map[key]
    return None

def omdb_film_oner(tur="action"):
    url = f"http://www.omdbapi.com/?apikey={OMDB_API_KEY}&type=movie&s={tur}"
    response = requests.get(url)
    data = response.json()

    if data.get("Response") == "True":
        filmler = [film["Title"] for film in data["Search"]]
        return "İşte bazı " + tur + " filmleri: " + ", ".join(filmler)
    else:
        return "Üzgünüm, şu anda öneri veremiyorum. Türü doğru girdiğinizden emin misin?"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def get_bot_response():
    if request.is_json:
        userText = request.get_json().get("message", "").lower()
    else:
        userText = request.form.get("message", "").lower()

    tur = get_tur_from_message(userText)
    if tur:
        cevap = omdb_film_oner(tur)
    else:
        cevap = "Hangi türde film istediğini belirtir misin? (örneğin: aksiyon, komedi)"

    return jsonify({"response": cevap})

if __name__ == "__main__":
    app.run(debug=True)

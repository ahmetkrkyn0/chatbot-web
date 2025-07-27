import requests

def test_omdb_api():
    apikey = "5d7d7304"
    tur = "action"
    url = f"http://www.omdbapi.com/?apikey={apikey}&type=movie&s={tur}"

    response = requests.get(url)
    data = response.json()

    if data.get("Response") == "True":
        filmler = [film["Title"] for film in data["Search"]]
        print("Bulunan filmler:")
        for film in filmler:
            print("-", film)
    else:
        print("Film bulunamadı veya API anahtarı geçersiz.")

if __name__ == "__main__":
    test_omdb_api()

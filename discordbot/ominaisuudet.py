import requests
import json
import credentials

def makaronilaatikko_resepti():
    return open("C://Users/leevi/Documents/Koulu/Ohjelmointi/ttc2030/harjoitustyö/makaronilaatikko.txt", "r", encoding="UTF-8").read()

def youtube_search(arg):
    r = requests.get(f"https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=1&q={arg}&type=video&key={credentials.YOUTUBE_TOKEN}")
    data = json.loads(r.text)
    return youtube_link(data["items"][0]["id"]["videoId"])

def youtube_link(id):
    return f"https://www.youtube.com/watch?v={id}"
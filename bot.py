import os, json, requests

TOKEN = os.environ["X_BEARER"]

def tweet(text):
    r = requests.post(
        "https://api.x.com/2/tweets",
        headers={
            "Authorization": f"Bearer {TOKEN}",
            "Content-Type": "application/json"
        },
        data=json.dumps({"text": text})
    )
    print(r.status_code, r.text)

with open("posts.txt", "r", encoding="utf-8") as f:
    lines = [l.strip() for l in f if l.strip()]

if not lines:
    print("Nada que publicar.")
    exit(0)

text = lines[0]
print("Publicando:", text)
tweet(text)

with open("posts.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(lines[1:]))

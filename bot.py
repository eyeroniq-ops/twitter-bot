import os, json, requests
from requests_oauthlib import OAuth1

auth = OAuth1(
    os.environ["X_API_KEY"],
    os.environ["X_API_SECRET"],
    os.environ["X_ACCESS_TOKEN"],
    os.environ["X_ACCESS_TOKEN_SECRET"],
)

def tweet(text):
    r = requests.post(
        "https://api.x.com/2/tweets",
        auth=auth,
        headers={"Content-Type": "application/json"},
        data=json.dumps({"text": text})
    )
    # Log útil
    print(r.status_code, r.text)
    r.raise_for_status()
    return r.json()

with open("posts.txt","r",encoding="utf-8") as f:
    lines=[l.strip() for l in f if l.strip()]

if not lines:
    print("Nada que publicar."); raise SystemExit(0)

text = lines[0]
print("Publicando:", text)
tweet(text)

with open("posts.txt","w",encoding="utf-8") as f:
    f.write("\n".join(lines[1:]))

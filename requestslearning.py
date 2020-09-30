import requests

try:
    res = requests.get("https://www.google.com/")
    content = res.content
    print(content)
except requests.ConnectionError:
    print("connection error")



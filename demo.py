import requests
res = requests.get('https://www.google.com.tw/')
print(res) 
print(res.status_code) # 200

if res.status_code == requests.codes.ok:
    print("OK")
    print(res.text)


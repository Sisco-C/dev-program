import requests
print("timeout = 0.001")
try:
    re = requests.get('https://www.imdb.com/title/tt0108778/', timeout = 0.001)
    print(re.text)
except requests.exceptions.RequestException as e:
    print(e)    
print("\ntimeout = 0.001")    
try:
    re = requests.get('https://www.imdb.com/title/tt0108778/', timeout = 0.001)
    print("Connected....!")
except requests.exceptions.RequestException as e:
    print(e)
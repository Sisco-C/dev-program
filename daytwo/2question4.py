import requests
response = requests.get('https://www.imdb.com/title/tt0108778/')
print("https://www.imdb.com/title/tt0108778/")
print(response.text)

print("\n")
print("\nContent :")
 # To print unicode response string 
print(response.content)
print("\n")
print("\nRaw data :")
re = requests.get('https://api.spoonacular.com/recipes/complexSearch', stream = True)
print(re.raw)

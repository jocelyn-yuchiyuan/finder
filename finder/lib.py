
import sys
import urllib.parse
import requests

BASE_URI = "www.refugerestrooms.org/api"
def search_toilet(query):
    url = f"https://www.refugerestrooms.org/api/v1/restrooms/search?page=1&per_page=10&offset=0&query={query}"
    response = requests.get(url).json()
    if  len(response) > 0 :
        street = response[0]["name"]
        return f"you can find a nice toilet here around tokyo: {street}"
    return "no toilets found"

#if __name__ == "__main__":
    #query = "tokyo"
    #street = search_toilet(query)
    #print(f"you can find a nice toilet here: {street}")

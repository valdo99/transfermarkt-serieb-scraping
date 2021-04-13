from bs4 import BeautifulSoup
import requests
import pandas as pd


#	PlayerProfiles = [player.PlayerData for player in df['Profile']]

def getPlayerPage(playerURL, saison):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}
    base = playerURL.replace("/profil/", "/leistungsdatendetails/")
    url = base + "/saison/"+saison
    try:
        print("Connecting...")
        response = requests.get(url, headers=headers)
        print("Connection successful, status code {}".format(response.status_code))
    except requests.exceptions.RequestException as e:
        print(e)
        exit()
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.content, 'html')
    # https://www.transfermarkt.it/matteo-gianello/profil/spieler/21686

    print(soup)


def main():
    getPlayerPage(
        "https://www.transfermarkt.it/matteo-gianello/profil/spieler/21686", '2001')


if __name__ == "__main__":
    main()

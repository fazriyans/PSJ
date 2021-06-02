from bs4 import BeautifulSoup
import requests

url = "https://www.bmkg.go.id/gempabumi/gempabumi-terkini.bmkg"

web = requests.get(url)
soup = BeautifulSoup(web.text, 'html.parser')

for td in soup.tbody.findAll('tr'):
    print("====================")
    data = td.findAll('td')
    print("no : " + (data[0].text))
    print("Waktu : " + (data[1].text))
    print("Lintang : " + (data[2].text))
    print("Bujur : " + (data[3].text))
    print("Magnitudo : " + (data[4].text))
    print("Kedalaman : " + (data[5].text))
    print("Wilayah : " + (data[6].text))
    print('\n')
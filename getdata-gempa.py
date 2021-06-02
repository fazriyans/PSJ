from bs4 import BeautifulSoup
import requests 

url = "https://www.bmkg.go.id/gempabumi/gempabumi-terkini.bmkg"

web = requests.get(url)
soup = BeautifulSoup(web.text, 'html.parser')

for td in soup.tbody.findAll('tr'):
    print("====================")
    data = td.findAll('td')
    print("no : " + (data[0].text))
    print("waktu : " + (data[1].text))
    print("lintang : " + (data[2].text))
    print("bujur : " + (data[3].text))
    print("magnitudo : " + (data[4].text))
    print("kedalaman : " + (data[5].text))
    print("wilayah : " + (data[6].text))
    print('\n')
    

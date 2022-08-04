import requests
from bs4 import BeautifulSoup
sa_url = 'https://www.sanantonio.gov/ParksAndRec/Parks-Facilities/All-Parks-Facilities/Buildings-Centers/PID/15292/ev/1/CategoryID/192/CategoryName/Community-Centers'

req = requests.get(sa_url)
soup_data = BeautifulSoup(req.text, 'html.parser')

# print(soup_data.body.form)

for article in soup_data.find_all("div", class_="article in_list span"):
    for content in article.find_all("div", class_="content"):
        for title in content.find_all("h2", class_="parkTitle"):
            print(title.select_one('a').text)

        for summary in content.find_all("div", class_="summary"):
            for br in summary.find_all("br")[0:3]:
                print(br.previousSibling)
        print('\n')
        
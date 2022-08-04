import requests
from bs4 import BeautifulSoup
sa_url = 'https://www.sanantonio.gov/ParksAndRec/Parks-Facilities/All-Parks-Facilities/Buildings-Centers/PID/15292/ev/1/CategoryID/192/CategoryName/Community-Centers'

req = requests.get(sa_url)
soup_data = BeautifulSoup(req.text, 'html.parser')

print(soup_data.body)

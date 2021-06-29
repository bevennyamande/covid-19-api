import requests
from itertools import islice
from bs4 import BeautifulSoup as bs
url = "https://www.mygov.in/corona-data/covid19-statewise-status/"
r  = requests.get(url)
htmlcontent = r.content
soup = bs(htmlcontent,	"html.parser")
# print(soup.prettify())
print("scrapping started")

# state name
state = [i for  i in soup.find_all("div",class_="field-name-field-select-state")]

state = [i.contents[1].string for i in state ]


# total confirmed
India_confirm = [i for  i in soup.find_all("div",class_="field-name-field-total-confirmed-indians")]
India_confirm = [i.contents[1].string for i in India_confirm ]

# cured
India_cured = [i for  i in soup.find_all("div",class_="field-name-field-cured")]
India_cured = [i.contents[1].string for i in India_cured ]


# deaths
India_deaths = [i for  i in soup.find_all("div",class_="field-name-field-deaths")]
India_deaths = [i.contents[1].string for i in India_deaths ]


desc = ["confirmed","cured","death"]





india_covid = {x.lower(): {y.lower():z for y, z in zip(desc,[India_confirm[ind],India_cured[ind],India_deaths[ind]])} for ind, x in enumerate([i for i in state])}
if __name__ == '__main__':
	print(india_covid)









import requests
from itertools import islice
from bs4 import BeautifulSoup as bs
url = "https://www.worldometers.info/coronavirus/country/us/"
r  = requests.get(url)
htmlcontent = r.content
soup = bs(htmlcontent,	"html.parser")
print("scrapping started")


country = [i.string for i in soup.find_all("a",class_="mt_a")[:51]]
# print(country)

names = ["sno",'state' , 'Totalcases', 'NewCases', 'TotalDeaths', 'NewDeaths', 'TotalRecovered',  'ActiveCases', 'TotCases/1M pop', 'Deaths/1M pop', 'TotalTests', 'Tests/1M pop']
tbody = soup.find("tbody")
country_info = [str(a.string) if a.string is not None else str(a.a.string) for i in tbody.find_all("tr")[1:] for a in i.find_all("td")[:12] ]
# country_info = [a if a != "\n" else "" for a  in country_info]

country_info = [a.replace("\n","") for a  in country_info]

usa_covid = {x.lower(): {y.lower():z for y, z in zip(names, country_info[ind*len(names):])} for ind, x in enumerate([i for i in country])}
if __name__ == '__main__':
	print(usa_covid)
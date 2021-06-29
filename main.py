import requests
from itertools import islice
from bs4 import BeautifulSoup as bs
import time
url = "https://www.worldometers.info/coronavirus/"
r  = requests.get(url)
htmlcontent = r.content
soup = bs(htmlcontent,	"html.parser")
print("scrapping started")

# total cases,deaths,recoveries
total = soup.find_all("div",class_="maincounter-number")
total = { k.lower():v for (k,v) in zip(["t_cases","t_death","t_recover"], [i.span.string for i in total])} 

# active and closed cases
t_info = { k.lower():v for (k,v) in zip(["infected","closed"],[i.string for i in soup.find_all("div",class_="number-table-main")])} 
t_active_detail = { k:v for (k,v) in zip(["mild","serious"],[i.string for i in soup.find_all("span",class_="number-table")[:2]])} 

# full country data
country = [i.string for i in soup.find_all("a",class_="mt_a")[:220]]
country.insert(196,"Cayman Islands")
country.insert(214,"MS Zaandam")

names = ["sno",'Country' , 'Totalcases', 'NewCases', 'TotalDeaths', 'NewDeaths', 'TotalRecovered', 'NewRecovered', 'ActiveCases', 'Serious', 'TotCases/1M pop', 'Deaths/1M pop', 'TotalTests', 'Tests/1M pop']
tbody = soup.find_all("tbody")[0]
country_info = [a.string if a.string is not None else "" for i in tbody.find_all("tr")[8:] for a in i.find_all("td")[:14] ]
covid_info = {x.lower(): {y.lower():z for y, z in zip(names, country_info[ind*len(names):])} for ind, x in enumerate([i for i in country])}

# latest news 
latest = [ i for i in soup.find_all("li",class_="news_li",limit=100)]
test = [ a for i in latest for a in islice(i.stripped_strings,None,5)]
for  i in range(len(test)):
	test[i:i+5] = [" ".join(test[i:i+5])]
test = test[:100:]
for  i in test:
	if "[" in i: 
		test[test.index(i)] = i[i.index("["):+1]
while("" in test) :
    test.remove("")

    
if __name__ == '__main__':
	print(covid_info)
	print(test)
	print(total)
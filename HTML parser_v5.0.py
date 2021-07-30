from bs4 import BeautifulSoup
import requests
check_source = requests.get('https://football.fantasysports.yahoo.com/f1/209056/draftresults')
print(check_source)
source = requests.get('https://football.fantasysports.yahoo.com/f1/209056/draftresults').text


soup = BeautifulSoup(source, 'lxml')
# print (soup)

tables = soup.find_all("table")
# draft_table = soup.find_all("table", class_ = "Table Table-interactive Table-px-med Fz-xxs")

print (tables)

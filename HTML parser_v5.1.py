from bs4 import BeautifulSoup
import requests
html_path = 'C:/Users/dan.mapes/Documents/GitHub/Python-search-top-200/__pycache__/view-source_https___football.fantasysports.html'

# source = requests.get('C:/Users/dan.mapes/Documents/GitHub/Python-search-top-200/__pycache__/view-source_https___football.fantasysports.html').text
with open(html_path,'r') as html_file:
    source = html_file.read()


    soup = BeautifulSoup(source, 'lxml')
    # print (soup.prettify())

    # tables = soup.find_all("table")
    draft_table = soup.find('table', class_='Table Table-interactive Table-px-med Fz-xxs')
    print (draft_table.prettify())

    draft_round = draft_table.find('th').text
    print (draft_round)
    draft_owners = draft_table.find_all('td', class_= 'last Px-sm')
    for draft_owner in draft_owners:
        drafted_player = draft_table.find('div', class_= 'emptyplayer')
        print (draft_owner.text)
        print (drafted_player.text)


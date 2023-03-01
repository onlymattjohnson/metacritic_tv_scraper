import requests
from bs4 import BeautifulSoup

def extract_genre(row):
    title_td = row.find('td', {'class': 'title'})
    if title_td:
        genre = title_td.find_next_sibling('td').text
        return genre
    return None

def extract_title(row):
    if row.find('td', {'class': 'title'}):
        return row.find('td', {'class': 'title'}).text
    return None

def extract_media_type(row):
    i = row.findAll('img')
    if i:
        return i[0]['alt']
    
    return None

def extract_network(row):
    i = row.findAll('img')
    if len(i) > 1:
        return i[1]['alt']
    
    return None

def extract_note(row):
    title_td = row.find('td', {'class': 'title'})
    if title_td:
        note_tr = row.find_next_sibling('tr')
        if note_tr:
            note_td = note_tr.find('td', {'class': 'notebig'})
            if note_td:
                return note_td.text
    return None

url = 'https://www.metacritic.com/feature/tv-premiere-dates'

# Thank you to Martijn Pieters at Stack Overflow [https://stackoverflow.com/questions/23651947/python-requests-requests-exceptions-toomanyredirects-exceeded-30-redirects]

s = requests.Session()
s.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'
r = s.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

# TV Shows
table_rows = soup.findAll('tr')

for table_row in table_rows:
    if table_row.find('th'):
        current_date = table_row.find('th').text
    elif table_row.find('td', {'class': 'title'}):
        show_title = extract_title(table_row)
        show_type = extract_media_type(table_row)
        show_network = extract_network(table_row)
        show_genre = extract_genre(table_row)
        show_note = extract_note(table_row)
        # print(table_row)
        print(f'Title: {show_title}, Type: {show_type}, Network: {show_network}, Genre: {show_genre}, Note: {show_note}')
        #note_td = table_row.find_next('td',{'class': 'notebig'})
        #print(note_td)
    else:
        x = None
        # print(table_row)
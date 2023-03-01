import requests
from bs4 import BeautifulSoup


url = 'https://www.metacritic.com/feature/tv-premiere-dates'

# Thank you to Martijn Pieters at Stack Overflow [https://stackoverflow.com/questions/23651947/python-requests-requests-exceptions-toomanyredirects-exceeded-30-redirects]

s = requests.Session()
s.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'
r = s.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

print(soup.prettify())
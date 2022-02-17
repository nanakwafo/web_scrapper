from bs4 import BeautifulSoup

with open('home.hml','r')  as  html_file:
    content = html_file.read()
    print(content)
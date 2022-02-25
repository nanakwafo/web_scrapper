from turtle import ht
from bs4 import BeautifulSoup
import requests 

html_text=requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
soup =BeautifulSoup(html_text,'lxml')
jobs = soup.find('li',class_= 'clearfix job-bx wht-shd-bx')
company_name = jobs.find('h3',class_='joblist-comp-name').text
print(company_name)
# with open('home.html','r')  as  html_file:
#     content = html_file.read()

#     soup =BeautifulSoup(content,'lxml')
#     course_cards = soup.find_all('div',class_= 'card')
#     for course in course_cards:
#         course_name =course.h5.text
#         course_price = course.a.text.split()[-1]

#         print(f'{course_name}  costs {course_price}')
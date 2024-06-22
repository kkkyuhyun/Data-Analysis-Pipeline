import requests 
from bs4 import BeautifulSoup

url="https://comic.naver.com/webtoon/weekday.nhn"
res=requests.get(url)
res.raise_for_status()

soup=BeautifulSoup(res.text,"lxml")
print(soup.title)
print(soup.title.get_text())
print(soup.a)#soup객체에서 처음 발견되는 a element를 반환한다
print(soup.a["href"])#a element 속성 '값' 정보를 출력한다.

 
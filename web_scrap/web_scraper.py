import requests 
from bs4 import BeautifulSoup

url="https://comic.naver.com/webtoon/weekday.nhn"
res=requests.get(url)
res.raise_for_status()

soup=BeautifulSoup(res.text,"lxml")
print(soup.title)
print(soup.title.get_text())
print(soup.a)#soup��ü���� ó�� �߰ߵǴ� a element�� ��ȯ�Ѵ�
print(soup.a["href"])#a element �Ӽ� '��' ������ ����Ѵ�.

 
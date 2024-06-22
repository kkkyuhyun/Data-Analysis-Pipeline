import csv
import requests 
from bs4 import BeautifulSoup

# 웹 크롤링한 파일 csv파일로 만들기
url = "https://finance.naver.com/sise/sise_market_sum.nhn"

filename = "Market_Capitalization 1~200.csv"
f = open(filename, "w", encoding="utf8", newline="")  # csv문단 띄어쓰기 방지
writer = csv.writer(f)

title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE	토론실".split("\t")

writer.writerow(title)  # 헤더 쓰기

params = {"sosok": 0, "page": 1}  # 페이지 번호를 쿼리 매개변수로 추가

res = requests.get(url, params=params)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

data_rows = soup.find("table", attrs={"class": "type_2"}).find("tbody").find_all("tr")
for row in data_rows:
    columns = row.find_all("td")
    if len(columns) <= 1:  # 의미 없는 데이터는 skip
        continue
    data = [column.get_text().strip() for column in columns]  # strip()으로 양쪽 공백 제거
    writer.writerow(data)

f.close()  # 파일 닫기


res = requests.get(url, params=params)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

data_rows = soup.find("table", attrs={"class": "type_2"}).find("tbody").find_all("tr")
for row in data_rows:
    columns = row.find_all("td")
    if len(columns) <=1: #의미 없는 데이터는 skip
        continue
    data = [column.get_text().strip() for column in columns]  # strip()으로 양쪽 공백 제거
    #print(data)
    writer.writerow(data)

import csv
import requests 
from bs4 import BeautifulSoup

# �� ũ�Ѹ��� ���� csv���Ϸ� �����
url = "https://finance.naver.com/sise/sise_market_sum.nhn"

filename = "Market_Capitalization 1~200.csv"
f = open(filename, "w", encoding="utf8", newline="")  # csv���� ���� ����
writer = csv.writer(f)

title = "N	�����	���簡	���Ϻ�	�����	�׸鰡	�ð��Ѿ�	�����ֽļ�	�ܱ��κ���	�ŷ���	PER	ROE	��н�".split("\t")

writer.writerow(title)  # ��� ����

params = {"sosok": 0, "page": 1}  # ������ ��ȣ�� ���� �Ű������� �߰�

res = requests.get(url, params=params)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

data_rows = soup.find("table", attrs={"class": "type_2"}).find("tbody").find_all("tr")
for row in data_rows:
    columns = row.find_all("td")
    if len(columns) <= 1:  # �ǹ� ���� �����ʹ� skip
        continue
    data = [column.get_text().strip() for column in columns]  # strip()���� ���� ���� ����
    writer.writerow(data)

f.close()  # ���� �ݱ�


res = requests.get(url, params=params)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

data_rows = soup.find("table", attrs={"class": "type_2"}).find("tbody").find_all("tr")
for row in data_rows:
    columns = row.find_all("td")
    if len(columns) <=1: #�ǹ� ���� �����ʹ� skip
        continue
    data = [column.get_text().strip() for column in columns]  # strip()���� ���� ���� ����
    #print(data)
    writer.writerow(data)

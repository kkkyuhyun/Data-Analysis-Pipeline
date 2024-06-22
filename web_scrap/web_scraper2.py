import requests
from bs4 import BeautifulSoup
import base64
import os
#Daumâ���� 2015����� 2019������� �� �������� ���� 5���� ��ȭ �̹����� �ٿ�ε�
#�ݺ����� ����Ͽ� ���� ���� �����͸� ������ ��, �̹��� �ٿ�ε� �κ��� �ݺ��� �ȿ� ���� �Ѵ�.

for year in range(2015, 2020):
    res = requests.get("https://search.daum.net/search?w=tot&q={}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR".format(year))
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')

    images = soup.find_all("img", attrs={"class": "thumb_img"})
    
    for idx, image in enumerate(images):
        image_url = image["src"]
        if image_url.startswith("//"):
            image_url = "https:" + image_url
        
        if image_url.startswith("data:image"):  # ������ URI ������ �̹����� ���
            image_data = base64.b64decode(image_url.split(",")[1])  # ������ ���ڵ�
            image_name = f"movies{year}_{idx + 1}.jpg"  # �̹��� ���� �̸� ����
            with open(image_name, "wb") as f:
                f.write(image_data)
            print(f"Downloaded image: {image_name}")
        else:
            image_res = requests.get(image_url)
            image_res.raise_for_status()
            with open(f"movies{year}_{idx + 1}.jpg", "wb") as f:
                f.write(image_res.content)
            print(f"Downloaded image: movies{year}_{idx + 1}.jpg")
        
        if idx >= 4:
            break  # �� �������� ���� 5�� �̹����� �ٿ�ε��ϰ� ����

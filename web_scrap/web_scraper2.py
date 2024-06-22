import requests
from bs4 import BeautifulSoup
import base64
import os
#Daum창에서 2015년부터 2019년까지의 각 연도별로 상위 5개의 영화 이미지를 다운로드
#반복문을 사용하여 여러 해의 데이터를 가져올 때, 이미지 다운로드 부분이 반복문 안에 들어가야 한다.

for year in range(2015, 2020):
    res = requests.get("https://search.daum.net/search?w=tot&q={}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR".format(year))
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')

    images = soup.find_all("img", attrs={"class": "thumb_img"})
    
    for idx, image in enumerate(images):
        image_url = image["src"]
        if image_url.startswith("//"):
            image_url = "https:" + image_url
        
        if image_url.startswith("data:image"):  # 데이터 URI 형식의 이미지인 경우
            image_data = base64.b64decode(image_url.split(",")[1])  # 데이터 디코드
            image_name = f"movies{year}_{idx + 1}.jpg"  # 이미지 파일 이름 설정
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
            break  # 각 연도별로 상위 5개 이미지만 다운로드하고 종료

import re
from bs4 import BeautifulSoup
import requests

def create_soup(url):
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "html.parser")
    return soup

def scrape_english():
    print("[English expression of today]")
    url = "https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english&keywd=haceng_submain_lnb_eng_I_others_english&logger_kw=haceng_submain_lnb_eng_I_others_english"
    soup = create_soup(url)
    sentences = soup.find_all("div", attrs={"id": re.compile("^conv_kor_t")})
    print("English Expression")
    for sentence in sentences[len(sentences)//2:]:
        print(sentence.get_text().strip())

if __name__ == "__main__":
    scrape_english()

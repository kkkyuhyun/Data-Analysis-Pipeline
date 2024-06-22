import requests
res=requests.get("http://google.com")
print("response code:",res.status_code)

if res.status_code==requests.codes.ok:
    print("Correct")
else:
    print("Problem.[error code",res.status_code,"]")
    
res.raise_for_status()
print("Continue Web Scraping")

print(len(res.text))
print(res.text)

with open("mygoogle.html","w",encoding="utf8") as f:
    f.write(res.text)

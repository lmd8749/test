import requests
from bs4 import BeautifulSoup

def getContant(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    #print(soup)
    results = soup.select('span.article-meta-value')
    if results:
        print('日期:', results[3].text)
        print('作者:', results[0].text)
        print('標題:', results[2].text)
        print('看板名稱:', results[1].text)
    print('內文:')
    a = soup.find_all("span", {"class": "f6"})
    print(a)

    #I will Remove the value that is not needed inside the text



r = requests.get("https://www.ptt.cc/bbs/MobileComm/index.html")
soup = BeautifulSoup(r.text, "html.parser")
sel = soup.select("div.title a")
"""for s in sel:
    print(s["href"], s.text)
    r2 = requests.get("https://www.ptt.cc/%s" % s["href"])
    soup2 = BeautifulSoup(r.text, "html.parser")
    sel2 = soup.select("div.title a")"""
for s in sel:
    url = "https://www.ptt.cc%s" % s.get("href")
    getContant(url)
    print("--------------")
"""
s= sel[0]
print(s["href"], s.text)
print(type(s["href"]))
print("https://www.ptt.cc%s" % s["href"])
r2 = requests.get("https://www.ptt.cc%s" % s["href"])
print(r2)
soup2 = BeautifulSoup(r2.text, "html.parser")
results = soup.select('span.article-meta-value')
print(results)
if results:
    print('作者:', results[0].text)
    print('看板:', results[1].text)
    print('標題:', results[2].text)
    print('時間:', results[3].text)
"""
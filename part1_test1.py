urls = [
    "http://www.google.com/a.txt",
    "http://www.google.com.tw/a.txt",
    "http://www.google.com/download/c.jpg",
    "http://www.google.co.jp/a.txt",
    "http://www.google.com/b.txt",
    "https://facebook.com/movie/b.txt",
    "http://yahoo.com/123/000/c.jpg",
    "http://gliacloud.com/haha.png",
]
countList = []
for url in urls:
    urlList = url.split("/")
    countList.append(urlList[-1])
countList.sort()
alreadyCountList = []
for obj in countList:
    if obj == "haha.png":
        continue
    elif obj not in alreadyCountList:
        print(obj, countList.count(obj))
        alreadyCountList.append(obj)
    else:
        continue

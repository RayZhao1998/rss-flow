import requests
import re
html = requests.get('https://blogroll.a2os.club/')
# print(html.text)

rss = re.findall('<td>(.*?)</td>',html.text)
f = open('rss.txt','w')
i = 1
for each in rss:
    if i%3==0 and each!='-':
        print(each, file=f)
    i+=1

def getrss():
    rss = re.findall('<td>(.*?)</td>', html.text)
    rsslist = []
    i = 1
    for each in rss:
        if i % 3 == 0 and each != '-':
            rsslist.append(each)
        i += 1
    return rsslist

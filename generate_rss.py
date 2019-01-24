import requests
import re
html = requests.get('https://blogroll.a2os.club/')

rss = re.findall('<td>(.*?)</td>',html.text)
f = open('rss.txt','w')
for i in range(len(rss)):
    if i % 3 == 0 and rss[i+2] != '-':
        author = re.search('>(.*?)<', rss[i]).group(1)
        print(author, file=f)
        print(rss[i+2], file=f)

def getrss():
    rss = re.findall('<td>(.*?)</td>', html.text)
    authorlist = []
    rsslist = []
    for i in range(len(rss)):
        if i % 3 == 0 and rss[i+2] != '-':
            author = re.search('>(.*?)<', rss[i]).group(1)
            authorlist.append(author)
            rsslist.append(rss[i+2])
    return (authorlist, rsslist)

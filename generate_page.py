# coding:utf-8
import feedparser
import time
from generate_rss import getrss
import ssl
if hasattr(ssl, '_create_unverified_context'):
    ssl._create_default_https_context = ssl._create_unverified_context

ArrayList = []

def AppendList(rss_url):
    feeds = feedparser.parse(rss_url)
    for SinglePost in feeds.entries:
        dict = {}
        dict['blog'] = feeds.feed.title
        dict['title'] = SinglePost.title
        dict['link'] = SinglePost.link
        dict['updated'] = time.strftime(
            "%Y-%m-%d %H:%M:%S", SinglePost.updated_parsed)
        ArrayList.append(dict)

def save_all_blogs_local():
    rsslist = getrss()
    for rss_url in rsslist:
        AppendList(rss_url)
    ArrayList.sort(key=lambda Adict: Adict['updated'], reverse=True)
    with open('rss.txt','r') as rss_f:
        lines = rss_f.readlines();
        for rss_url in lines:
            AppendList(rss_url)
    ArrayList.sort(key=lambda Adict: Adict['updated'], reverse=True)
    f = open("./index.txt", 'w', encoding='utf-8')
    for blog in ArrayList:
        print(blog['title']+" "+blog['blog'], file=f)
        print(blog['link'], file=f)
        print("update time: " + blog['updated'], file=f)


def get_first_10_blogs():
    rsslist = getrss()
    for rss_url in rsslist:
        AppendList(rss_url)
    ArrayList.sort(key=lambda Adict: Adict['updated'], reverse=True)
    return ArrayList[:9]

if __name__ == "__main__":
    save_all_blogs_local()

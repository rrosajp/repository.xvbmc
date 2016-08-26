# -*- coding: utf-8 -*-
import requests,re,urllib2
import json
from bs4 import BeautifulSoup

def getPage(url):
    r = requests.get(url)

    soup = BeautifulSoup(r.text,'html5lib')
    links =  soup.find('div', {"id": "content"})
    
    li = links.findAll('li', {"class":lambda x: x and "border-radius-" in x})

    seriesList = []
    for link in li:
        seriesList.append({'title':link.find('a').text,'url':link.find('a').get('href'),'thumbnail':link.find('img').get('src')})
    
    try:
        next = soup.find('a', text=lambda x: x and 'next' in x.lower()).get('href')
    except:
        next = None
    if next != None:
        seriesList.append({'title':"Next","url":next})
    
    return seriesList
     


def getStreams(url):
    headers = {}
    headers['User-Agent']= 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20'
    request = urllib2.Request(url,headers=headers)
    resp = urllib2.urlopen(request)
    result = resp.read()
    soup = BeautifulSoup(result,'html5lib')
    soup.prettify()
    links =  soup.find('div', {"class": "video-embed"})
    embed = links.find('iframe').get('src')

    return getStreamLinks(embed)

def getStreamLinks(url):
    headers = {}
    headers['User-Agent']= 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20'
    request = urllib2.Request(url,headers=headers)
    resp = urllib2.urlopen(request)
    result = resp.read()
    content = re.compile('\"sources\"\:(.*)\,\"logo\"').findall(result)[0]
    sources = json.loads(content)
    return sources

def search(query):
    return getPage("http://moviepool.net/?s="+query.replace(" ","+"))

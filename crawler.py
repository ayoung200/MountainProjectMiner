import sys
import re
import urllib2
import urlparse
from HTMLParser import HTMLParser
ROOT_PAGE = 'http://www.mountainproject.com'
pagesToCrawl = ['http://www.mountainproject.com/destinations/']
pagesAlreadyCrawled = set()

class RouteData:
    def __init__(self, url, state, longlat, name, routeType, height):
        self.state = state
        self.longlat = longlat
        self.name = name
        self.routeType = routeType
        self.height = height
        

class MountainProjectParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        #print tag, attrs
        if tag=='a':
            link = ''
            for attribute in attrs:
                if attribute[0] == 'href':
                    link = attribute[1]
            linkParts = link.split('/')
            if len(linkParts)==4 and linkParts[1]=='v' and linkParts[3].isdigit():
                page = ROOT_PAGE+link
                if not page in pagesAlreadyCrawled:
                    pagesToCrawl.append(page)
                    name = linkParts[2]
                    print name
    def handle_data(self,data):
        if self.get_starttag_text()=='tr':
            index = data.find("Type:")
            d = data.find('<td>')
    #def handle_data(self,data):
    #    if self.get_starttag_text()=="td":
    #        print data
mtnParser = MountainProjectParser()

while len(pagesToCrawl)>0:
	currentPage = pagesToCrawl.pop()
	pagesAlreadyCrawled.append(currentPage)
	url = urlparse.urlparse(currentPage)
	response = urllib2.urlopen(currentPage).read()

	mtnParser.feed(response)
	
	


#!/usr/bin/env python
#encoding: utf8
import urllib2
import urllib
import re

def getHtml(url):
	return urllib2.urlopen(url).read()

def getImg(html):
	x=0	
	reg=r'<img.*src=\"(ht.*)\".*'
	imgre=re.compile(reg)
	imglist=re.findall(imgre,html)
	for imgurl in imglist:
		print imgurl
		urllib.urlretrieve(imgurl,'meinv%d.jpg' %x)
		x+=1
		

for i in range(1,2):
	try: 
		html= getHtml("http://web.toutiao.com/a3631468051/")
		getImg(html)
	except urllib2.HTTPError:
		print "URL 不存在"




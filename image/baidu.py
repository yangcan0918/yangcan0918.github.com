#!/usr/bin/env python
#encoding: utf8
import urllib2
import urllib
import re

def getHtml(url):
	return urllib2.urlopen(url).read()

def getImg(html,x):
	if x < 700:
	     reg=r'<img.*src=\"(ht.*.jpg)\".*'
	else:
	     reg=r'<img.*src=\"(ht.*/middle)\".*'
	imgre=re.compile(reg)
	imglist=re.findall(imgre,html)
	for imgurl in imglist:
		print imgurl
		urllib.urlretrieve(imgurl,'baidu/meinv%d.jpg' %x)
		

for i in range(100,10000):
	try: 
		html= getHtml("http://loudatui.com/items/%d" %i)
		getImg(html,i)
		print i
	except urllib2.HTTPError:
		print "URL 不存在"




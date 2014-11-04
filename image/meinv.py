#!/usr/bin/env python
#encoding: utf8
import urllib2
import urllib
import re

def getHtml(url):
	return urllib2.urlopen(url).read()

def gegImg(html):
	reg=r'<img alt="Middle" class="img" src=\"(.*?)\"/>'
	imgre=re.compile(reg)
	imglist=re.findall(imgre,html)
	#x=0
	for imgurl in imglist:
		print imgurl
	#	urllib.urlretrieve(imgurl,'美女%s.jpg' %x)
	#	x+=1

html= getHtml("http://loudatui.com/items/1106")
html = urllib.urlopen(html).read().decode('utf-8')
getImg(html)

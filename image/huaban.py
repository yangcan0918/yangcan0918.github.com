#!/usr/bin/env python
#encoding: utf8
import urllib2
import urllib
import re

def getHtml(url):
	return urllib2.urlopen(url).read()
num=0
def getImg(html):
	global num
	reg=r'.*"orig_source":"(http://.*/.*.jpg)"'
	imgre=re.compile(reg)
	imglist=re.findall(imgre,html)
	for imgurl in imglist:
		print imgurl
		urllib.urlretrieve(imgurl,'meinv/huaban%d.jpg' %num)
		num=num+1
		

for i in range(200000005,400000000):
	try: 
	
		print i
		html= getHtml("http://huaban.com/pins/%d" %i)
		getImg(html)
	except (urllib2.HTTPError,IOError):
		print "URL 不存在"




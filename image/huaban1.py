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
	reg=r'.*/pins/(.*)/".*>'
	imgre=re.compile(reg)
	imglist=re.findall(imgre,html)
	print imglist
	for imgurl in imglist:
		print imgurl
		#urllib.urlretrieve(imgurl,'meinv/huaban%d.jpg' %num)
		#num=num+1
		

for i in range(10000,10001):
	try: 
		i=2373671564564
		#html= getHtml("http://loudatui.com/items/%d" %i)
		html= getHtml("http://huaban.com/boards/16480581/?md=newbn&beauty")
		print html
		getImg(html)
	except urllib2.HTTPError:
		print "URL 不存在"




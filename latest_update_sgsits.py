from bs4 import BeautifulSoup
import urllib.request,urllib.parse,urllib.error
import ssl

ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

url="http://www.sgsits.ac.in/"
html=urllib.request.urlopen(url,context=ctx).read()
soup=BeautifulSoup(html,'html.parser')

tag1=soup.find(id='yt_wrapper')

a=tag1.find(id="yt_spotlight5")
b=a.find(class_='container')
c=b.find(class_='row')
d=c.find(id='top6')
e=d.find('div')
f=e.find('div')
g=f.find('div')
h=g.find(class_='slider')
i=h.find('div')
j=i.find('div')
k=j.find(class_='vpi-wrap')
perform=k('div',{'class':'item'})
#print(perform[0:4])
for tag in perform:
		#print(tag)
		l=tag.find('div',{'class':'item-wrap'})
		m=l.find(class_='item-info')
		#print(almos)
		n=m.find(class_='item-inner')
		o=n.find(class_='item-content')
		news=o.find(class_='item-des')
		latestupdate=news.find('strong')
		print(latestupdate.text,latestupdate.next_sibling)
		link=latestupdate.find('a')
		print(link.get('href'))
		print('\n------------------------------------------')


		

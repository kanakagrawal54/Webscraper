from bs4 import BeautifulSoup
import urllib.request,urllib.parse,urllib.error
import ssl

ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

url="http://www.sgsits.ac.in/"
html=urllib.request.urlopen(url,context=ctx).read()
soup=BeautifulSoup(html,'html.parser')

tag1=soup.find(id='yt_wrapper').find(id="yt_spotlight5")
outerbox=tag1.find(class_='container').find(class_='row')
innerbox=outerbox.find(id='top6').div.div.find(class_='slider')
i=innerbox.div.div.find(class_='vpi-wrap')
perform=i('div',{'class':'item'})

for tag in perform:
		l=tag.find('div',{'class':'item-wrap'})
		m=l.find(class_='item-info').find(class_='item-inner')
		news=m.find(class_='item-content').find(class_='item-des')
		latestupdate=news.find('strong')
		print(latestupdate.text)
		link=latestupdate.find('a')
		print(link.get('href'))
		print('\n------------------------------------------')


		

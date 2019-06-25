import requests
import hashlib
from bs4 import BeautifulSoup
import datetime
import csv
from random import choice


headers=[{'accept':'*/*',
		'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
		},
		{'accept':'*/*',
		'user-agent': 'Mozilla/5.0 (Windows NT 6.1; rv:67.0) Gecko/20100101 Firefox/67.0'
		},
		{'accept':'*/*',
		'user-agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.172 Safari/537.36 Vivaldi/2.5.1525.46'
		},
		{'accept':'*/*',
		'user-agent':'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)'
		},
		{'accept':'*/*',
		'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.56 Safari/536.5'
		},
		{'accept':'*/*',
		'user-agent':'Mozilla/5.0 (Macintosh; I; Intel Mac OS X 10_6_7; ru-ru) AppleWebKit/534.31+ (KHTML, like Gecko) Version/5.0.5 Safari/533.21.1'
		}
		]

#User-Agent: Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)
#User-Agent: Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)

def get_proxy():
	url='https://free-proxy-list.net/'
	session=requests.Session()
	request=session.get(url, headers=choice(headers))
	if request.status_code==200:
		soup=BeautifulSoup(request.content,'lxml')
	else:
		print('ERROR', request.status_code)
	tb_rows = soup.find('table', id='proxylisttable').find('tbody').find_all('tr')[1:12]
	
	proxy_list=[]
	for tr in tb_rows:
		rdata=tr.find_all('td')
		
		ip=rdata[0].text.strip()
		port=rdata[1].text.strip()
		prot='https' if 'yes' in rdata[6].text.strip() else 'http'
		proxy={'protocol':prot, 'ip': ip+':'+port }
		final_proxy={proxy['protocol']: proxy['ip']}
		
		proxy_list.append(final_proxy)
	#print(choice(proxy_list))
	return choice(proxy_list)

def transform_date(data):
	today=datetime.date.today()
	if 'Сегодня' in data:
		elem=data.replace('Сегодня', str("{}.{}.{}".format(today.day, today.month, today.year)))
		return elem
	if 'Вчера' in data:
		elem=data.replace('Вчера', str("{}.{}.{}".format(today.day-1, today.month, today.year)))
		return elem
	else:
		return data	
	
	


def write_csv(data, file_name):
	with open(file_name, 'a', newline='', encoding='utf-8-sig') as f:
		writer = csv.DictWriter(f, fieldnames=fieldnames)
		for note in data:
			writer.writerow(note)
	

def get_page(url, hd, pr):
	header=hd
	proxy=pr
	print(header)
	print(proxy)
	session=requests.Session()
	request=session.get(url, headers=header, proxies=proxy)
	if request.status_code==200:
		soup=BeautifulSoup(request.content,'lxml')
		return soup
	else:
		print('ERROR', request.status_code)
	 

def get_html(soup, file_name): #  передает имя файла для записи и перезаписи
	block=soup.find_all('div', class_='item_table-wrapper')
	arr=[]
	for item in block:
		data = {'id': get_id(find_link(item)),
						'name': ' '.join(find_vacans(item).split()),
						'wage': find_wage(item),
						'date': transform_date(find_date(item)),
						'town': find_town(item),
						'firm': ' '.join(find_firm(item).split()),
						'link': find_link(item)
						}
		arr.append(data)
	write_csv(arr, file_name)
	
	
	

def find_vacans(link):
	vacant=link.find('a', class_='item-description-title-link')
	elem=vacant.text
	#print(elem)
	return elem.lower()

def find_wage(link):
	wage=link.find('span', class_='price')
	elem=wage.get('content')
	#print(elem)
	return int(elem)

def find_date(link):
	date=link.find('div', class_='js-item-date')
	elem=date.get('data-absolute-date')
	#print(elem)	
	return elem

def find_link(link):
	a=link.find('a', class_='item-description-title-link')
	elem='https://www.avito.ru' + a.get('href')
	#print(elem)	
	return elem

def get_id (link):
	id=hashlib.sha1(bytes(link, encoding= 'utf-8')).hexdigest()
	#print(id)	
	return id

def find_town(link):
	p=link.find('div', class_='data')
	block_text=p.find_all('p')
	#print(block_text[2])	
	dirty_text=' '.join(block_text[2].text.split())
	
	#print(dirty_text)	
	text = dirty_text.replace('(','').replace(')','')
	#print(text)	
	return text

def find_firm(link):
	p=link.find('div', class_='data')
	elem=p.find_all('p')
	#print(elem)	
	return elem[1].text

def get_pagination_last(url,hd, pr):
	fir_page='1'
	url = url.format(str(fir_page))
	soup=get_page(url,hd,pr)
	pag_list=soup.find_all('a', class_='pagination-page')
	
	for pag in pag_list:
		text_checker=pag.text
		
		if 'Последняя' in text_checker:
			last_url=pag.get('href').split('=')[1]
			
			return int(last_url)
		else:
			continue

def main(file_name):
	areas=['https://www.avito.ru/voronezhskaya_oblast/vakansii?p={}',
			'https://www.avito.ru/nizhegorodskaya_oblast/vakansii?p={}',
			'https://www.avito.ru/saratovskaya_oblast/vakansii?p={}'
			
			]
	
	
	for pattern in areas:
		proxy=get_proxy()
		head=choice(headers)
		
		last_count=get_pagination_last(pattern, head, proxy)
		for i in range(1, 2): #last_count
			url = pattern.format(str(i))
			
			get_html(get_page(url, head,proxy), file_name)
	
	

#'https://www.avito.ru/nizhegorodskaya_oblast/vakansii?p={}' 5 604
#'https://www.avito.ru/saratovskaya_oblast/vakansii?p={}'  4 196 
#'https://www.avito.ru/voronezhskaya_oblast/vakansii?p={}'  4 882
#'https://www.avito.ru/yaroslavskaya_oblast/vakansii?p={}'  2 173
#'https://www.avito.ru/tverskaya_oblast/vakansii?p={}'  2 732
#'https://www.avito.ru/moskovskaya_oblast/vakansii?p={}'
#'https://www.avito.ru/bryanskaya_oblast/vakansii?p={}'
#'https://www.avito.ru/tulskaya_oblast/vakansii?p={}'	
#'https://www.avito.ru/kaluzhskaya_oblast/vakansii?p={}'		
		
if __name__ == "__main__":
	today=datetime.datetime.now()
	file_name= str("./work_files/kaluga_vakans/Voronezh&obl_vakant_{}_{}_{}__{}_{}".format(today.day, today.month, today.year, today.hour,today.minute )) + '.csv'
	fieldnames = ['id','name','wage','date','town','firm','link']
	with open(file_name, 'a', newline='', encoding='utf-8-sig') as f:
		writer = csv.DictWriter(f, fieldnames=fieldnames)
		writer.writeheader()
	main(file_name)

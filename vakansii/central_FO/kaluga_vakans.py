import requests
import hashlib
from bs4 import BeautifulSoup
import datetime
import csv

headers={'accept':'*/*',
		'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}


def transform_date(data):
	today=datetime.date.today()
	if 'Сегодня' in data:
		elem=data.replace('Сегодня', str("{}.{}.{}".format(today.day, today.month, today.year)))
		return elem
		#print(elem)
	if 'Вчера' in data:
		elem=data.replace('Вчера', str("{}.{}.{}".format(today.day-1, today.month, today.year)))# datetime.date.today().day-1
		return elem
		#print(elem)
		#print("{}.{}.{}".format(today.day, today.month, today.year))      # 2.5.2017
	else:
		return data	
	
	


def write_csv(data):
	today=datetime.datetime.now()
	file_name= str("./work_files/kaluga_vakans/kaluga&obl_vakant_{}_{}_{}__{}_{}".format(today.day, today.month, today.year, today.hour,today.minute )) + '.csv'
	fieldnames = ['id','name','wage','date','town','firm','link']
	with open(file_name, 'a', newline='', encoding='utf-8-sig') as f:
		writer = csv.DictWriter(f, fieldnames=fieldnames)
		writer.writeheader()
		for note in data:
			writer.writerow(note)
		


def get_page(url):
	headers={'accept':'*/*',
		'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
	session=requests.Session()
	request=session.get(url, headers=headers)
	if request.status_code==200:
		soup=BeautifulSoup(request.content,'html.parser')
		return soup
	else:
		print('ERROR', request.status_code)
	 

def get_html(soup):
	block=soup.find_all('div', class_='item_table-wrapper')
	page_count=soup.find_all('a', class_='pagination-page')
	arr=[]
	for item in block:
		data = {'id': get_id(find_link(item)),
					'name': ' '.join(find_vacans(item).split()),
					'wage': find_wage(item),
					'date': transform_date(find_date(item)),
					'town': ' '.join(find_town(item).split()),
					'firm': ' '.join(find_firm(item).split()),
					'link': find_link(item)
					}
		arr.append(data)
	write_csv(arr)
	
				
	

def find_vacans(link):
	vacant=link.find('a', class_='item-description-title-link')
	elem=vacant.text
	#print(elem)
	return elem

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
	elem=p.find_all('p')
	#print(elem)	
	return elem[2].text

def find_firm(link):
	p=link.find('div', class_='data')
	elem=p.find_all('p')
	#print(elem)	
	return elem[1].text

def get_pagination_last(url):
	fir_page='1'
	url = url.format(str(fir_page))
	soup=get_page(url)
	pag_list=soup.find_all('a', class_='pagination-page')
	
	for pag in pag_list:
		text_checker=pag.text
		
		if 'Последняя' in text_checker:
			last_url=pag.get('href').split('=')[1]
			
			return int(last_url)
		else:
			continue

def main():
	areas=['https://www.avito.ru/kaluga/vakansii?p={}']
	
	
	for pattern in areas:
		last_count=get_pagination_last(pattern)
		for i in range(1, 3):
			url = pattern.format(str(i))
			get_html(get_page(url))
	
			
		
if __name__ == "__main__":
	main()

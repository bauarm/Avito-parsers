import requests
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
	today=datetime.date.today()
	file_name= str("{}_{}_{}_moskva_vakansii".format(today.day, today.month, today.year)) + '.csv'
	#print(file_name)
	with open(file_name, 'a', newline='') as f:
		writer = csv.writer(f)
		writer.writerow((data['name'],
                         data['wage'],
                         data['date'],
                         data['town'],
						 data['firm'],
						 data['link']
						 ))
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
	print('pages' + str(len(page_count)))
	print(len(block))
	#print('*******')
	try:
		for item in block:
			data = {'name': find_vacans(item),
					'wage': find_wage(item),
					'date': transform_date(find_date(item)),
					'town': ' '.join(find_town(item).split()),
					'firm': ' '.join(find_firm(item).split()),
					'link': find_link(item)
					}
			write_csv(data)
	except:
			print('error')		
	

def find_vacans(link):
	vacant=link.find('a', class_='item-description-title-link')
	elem=vacant.text
	#print(elem)
	return elem

def find_wage(link):
	wage=link.find('span', class_='price')
	elem=wage.get('content')
	#print(elem)
	return elem

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

def main():
	areas=['https://www.avito.ru/moskva/vakansii?p={}']
	
	try:
		for pattern in areas:
			for i in range(1, 6):
				print('*****',i ,'*******')
				url = pattern.format(str(i))
				get_html(get_page(url))
	except:
			print('error main loop')
		
if __name__ == "__main__":
	main()

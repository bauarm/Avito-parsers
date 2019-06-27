import os
import csv
import re

loader=[{'name': 'Грузчик', 'key_word': 'грузч'},{'name': 'Транспортировщик', 'key_word': 'транспортировщ'},{'name': 'Экспедитор', 'key_word': 'экспедитор'},
		{'name': 'Наборщик', 'key_word': 'наборщ'},{'name': 'Прессовщик', 'key_word': 'прессовщ'},{'name': 'Приемщик', 'key_word': 'приемщ'},
		{'name': 'Комплектовщик', 'key_word': 'комплектовщ'},{'name': 'Укладчик', 'key_word': 'укладч'},{'name': 'Упаковщик', 'key_word': 'упаковщ'},
		{'name': 'Стикеровщик', 'key_word': 'стикеровщ'},{'name': 'Сборщик', 'key_word': 'сборщ'},{'name': 'Работник торгового зала', 'key_word': 'работник торгового зала'},
		
		{'name': 'Продавец', 'key_word': 'продав'},{'name': 'Кассир', 'key_word': 'кассир'},{'name': 'Продавец-консультант', 'key_word': 'консультант'},
		{'name': 'Водитель', 'key_word': 'водит'},{'name': 'Таксист', 'key_word': 'такс'},{'name': 'Дальнобойшик', 'key_word': 'дальноб'},
		{'name': 'Разнорабочий', 'key_word': 'разнораб'},{'name': 'Подсобник', 'key_word': 'подсоб'},{'name': 'Охранник', 'key_word': 'охран'},
		{'name': 'Менеджер', 'key_word': 'менедж'},{'name': 'Оператор', 'key_word': 'оператор'},{'name': 'Повар', 'key_word': 'повар'},
		{'name': 'Администратор', 'key_word': 'администрат'},{'name': 'Рабочий', 'key_word': 'рабоч'},{'name': 'Официант', 'key_word': 'официант'},
		
		{'name': 'Кладовщик', 'key_word': 'кладовщ'},{'name': 'Мастер', 'key_word': 'маст'},{'name': 'Мерчендайзер', 'key_word': 'мерченд'},
		{'name': 'Парикмахер', 'key_word': 'парикмах'},{'name': 'Уборщик', 'key_word': 'уборщ'},{'name': 'Автослесарь', 'key_word': 'автослес'}
		
		
		]

no_loader=['погрузч']

def write_csv(data, file_name):
	fieldnames = ['id','post','wage']
	with open(file_name, 'a', newline='', encoding='utf-8-sig') as f:
		writer = csv.DictWriter(f, fieldnames=fieldnames)
		for note in data:
			writer.writerow(note)
		
def write_csv2(data, file_name):
	fieldnames = ['id', 'prof','count','min_wage','max_wage','average']
	with open(file_name, 'a', newline='', encoding='utf-8-sig') as f:
		print(data)
		writer = csv.DictWriter(f, fieldnames=fieldnames)
		
		for note in data:
			#print(note)
			writer.writerow(note)	

def csv_dict_reader(data_set):
	arr=[]
	arr_wage=[]
	with open(data_set, mode='r', newline="", encoding='utf-8-sig') as f_obj:
		reader = csv.DictReader(f_obj, delimiter=',')
		for line in reader:
			#print(line)
			profs={'id':(line['id']),
					'post':(line['name']),
					'wage':int((line['wage']))
				}
			arr.append(profs)
	return arr
	
	
	
def prof_finder(vacant_key, vacant_full, vac_file_name, data_set):
	prof=vacant_key
	arr=csv_dict_reader(data_set)
	wage_result=[]
	prof_result=[]
	pivot_result=[]
	wage_sum=0
	count=0
	for dol in arr:
		result = re.search(prof, str(dol['post']))
		
		if type(result) == re.Match:
			if dol['wage']>8000:
				#print(dol)
				profs_target={'id':(dol['id']),
				
							'post':(dol['post']),
							'wage':(dol['wage'])
							}
				prof_result.append(profs_target)
				wage_result.append(dol['wage'])
				count+=1
				try:
					wage_sum+=dol['wage']
				except Exception as e:
					print(e.__class__)
	try:	
		min_wage=min(wage_result)
		max_wage=max(wage_result)
		averg=wage_sum//len(wage_result)
		#print(prof,' ',' ',count,' ','MIN__',min_wage,',','MAX__',max_wage,',','AVERG__',averg)
		pivot_table={'id':(dol['id']),
					'prof':(vacant_full),
					'count':(count),
					'min_wage':(min_wage),
					'max_wage':(max_wage),
					'average':(averg)
					}
		pivot_result.append(pivot_table)
	except Exception as e:
		print(e.__class__)
	print(prof_result)
	print(pivot_result)
	write_csv(prof_result, 'gruzch_moscow_obl_6_2019.csv')
	write_csv2(pivot_result, vac_file_name+'.csv')
	
def main(this_file):
	for work in loader:
		#print(len(loader))
		#print(work)
		prof_finder(work['key_word'],work['name'],loader[0]['name'],this_file)
	
if __name__ == "__main__":
	curDir=os.getcwd()
	files = os.listdir(curDir+"\\data")
	#print(files)
	for file in files:
		this_file=(curDir+"\\data"+"\\"+file)
		main(this_file)
	
	
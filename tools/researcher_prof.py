import csv
import re

loader=[{'name': 'грузчик', 'key_word': 'грузч'},{'name': 'транспортировщик', 'key_word': 'транспортировщ'},{'name': 'экспедитор', 'key_word': 'экспедитор'},
		{'name': 'наборщик', 'key_word': 'наборщ'},{'name': 'прессовщик', 'key_word': 'прессовщ'},{'name': 'приемщик', 'key_word': 'приемщ'},
		{'name': 'комплектовщик', 'key_word': 'комплектовщ'},{'name': 'укладчик', 'key_word': 'укладч'},{'name': 'упаковщик', 'key_word': 'упаковщ'},
		{'name': 'стикеровщик', 'key_word': 'стикеровщ'},{'name': 'сборщик', 'key_word': 'сборщ'},{'name': 'работник торгового зала', 'key_word': 'работник торгового зала'},
		
		{'name': 'продавец', 'key_word': 'продав'},{'name': 'кассир', 'key_word': 'кассир'},{'name': 'продавец-консультант', 'key_word': 'консультант'},
		{'name': 'Водитель', 'key_word': 'водит'},{'name': 'таксист', 'key_word': 'таксист'},{'name': 'дальнобойшик', 'key_word': 'дальноб'},
		{'name': 'Разнорабочий', 'key_word': 'разнораб'},{'name': 'Подсобник', 'key_word': 'подсоб'},{'name': 'Охранник', 'key_word': 'охран'}
		]

no_loader=['погрузч']

def write_csv(data, file_name):
	fieldnames = ['post','wage']
	with open(file_name, 'a', newline='', encoding='utf-8-sig') as f:
		writer = csv.DictWriter(f, fieldnames=fieldnames)
		for note in data:
			writer.writerow(note)
		
def write_csv2(data, file_name):
	fieldnames = ['id', 'prof','count','min_wage','max_wage','average']
	with open(file_name, 'a', newline='', encoding='utf-8-sig') as f:
		#print(data)
		writer = csv.DictWriter(f, fieldnames=fieldnames)
		
		for note in data:
			print(note)
			writer.writerow(note)	

def csv_dict_reader():
	arr=[]
	arr_wage=[]
	with open('Kaluga&obl_vakant_21_6_2019__23_28.csv', mode='r', newline="", encoding='utf-8-sig') as f_obj:
		reader = csv.DictReader(f_obj, delimiter=',')
		for line in reader:
			#print(line)
			profs={'id':(line['id']),
					'post':(line['name']),
					'wage':int((line['wage']))
				}
			arr.append(profs)
	return arr
	
	
	
def prof_finder(vacant_key, vacant_full, vac_file_name):
	prof=vacant_key
	arr=csv_dict_reader()
	wage_result=[]
	prof_result=[]
	pivot_result=[]
	wage_sum=0
	count=0
	for dol in arr:
		result = re.search(prof, str(dol['post']))
		
		if type(result) == re.Match:
			if dol['wage']>8000:
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
	
	
	write_csv(prof_result, 'gruzch_moscow_obl_6_2019.csv')
	write_csv2(pivot_result, vac_file_name+'.csv')
	
def main():
	for work in loader:
		prof_finder(work['key_word'],work['name'],loader[0]['name'])
	
if __name__ == "__main__":
	main()
	
	
import csv
import re


#otbor_taxist=['водитель','водитель яндекс','водитель uber','водитель такси','таксист'] # по нулевому индекс идет первомоночальный отбор ,бинарныйпоиск?
otbor_taxist=['водител']
gazelist=['водител газел','водитель фотон','водитель грузчик','водитель курьер','водитель экспедитор']
taxist=['водитель яндекс','водитель uber','водитель такси','таксист']
dalnoboy=['водител газел','водитель фотон','водитель грузчик','водитель курьер','водитель экспедитор']

def write_csv(data, file_name):
	fieldnames = ['post','wage']
	with open(file_name, 'a', newline='', encoding='utf-8-sig') as f:
		#print(data)
		writer = csv.DictWriter(f, fieldnames=fieldnames)
		
		for note in data:
			print(note)
			writer.writerow(note)
		


def csv_dict_reader():
	arr=[]
	arr_wage=[]
	with open('Tula&obl_vakant_23_6_2019__11_36.csv', mode='r', newline="", encoding='utf-8-sig') as f_obj:
		reader = csv.DictReader(f_obj, delimiter=',')
		
		for line in reader:
			#print(line)
			profs={'post':(line['name']),
				'wage':int((line['wage']))
				}
			arr.append(profs)
	dol_cnt=0
	prof='водител'
	wage_result=[]
	wage_sum=0
	for dol in arr:
		result = re.search(prof, str(dol['post']))
		
		if type(result) == re.Match:
			if dol['wage']>9000:
				#print(dol['wage'])
				wage_result.append(dol['wage'])
				wage_sum+=dol['wage']
			#print(result.string,',',dol['wage'])
			#print(result.string,' ')
		dol_cnt+=1
	min_wage=min(wage_result)
	max_wage=max(wage_result)
	averg=wage_sum//len(wage_result)
	#print('MIN__',min_wage,',','MAX__',max_wage,',','AVERG__',averg)
	write_csv(arr, 'vacancies&salaries_tula&obl_6_2019.csv')
	#return profs
		
 
#функция собирает общий пул похожих профессий по регионы, по корню слова
#функция которая кроит общий пул на зараннее определенные специлизации
#функция ыспомогательная находит профессии которые еще не известны приложению и заносит их в отдельлный список
# нужен сбор айди чтобы вытягивать из базы некоторые эллементы по нему

def otbor(arr, csvf):
	sorted(csvf)
	main_key=arr[0]
	
if __name__ == "__main__":
	csv_dict_reader()
	
	
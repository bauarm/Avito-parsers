import csv
import re


#otbor_taxist=['водитель','водитель яндекс','водитель uber','водитель такси','таксист'] # по нулевому индекс идет первомоночальный отбор ,бинарныйпоиск?
otbor_taxist=['водител']
gazelist=['водител газел','водитель фотон','водитель грузчик','водитель курьер','водитель экспедитор',' ',' ']

 
def csv_dict_reader():
	arr=[]
	arr_wage=[]
	with open('kaluga&obl_vakant_21_6_2019__23_28.csv', mode='r', newline="", encoding='utf-8-sig') as f_obj:
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
				print(dol['wage'])
				wage_result.append(dol['wage'])
				wage_sum+=dol['wage']
			#print(result.string,',',dol['wage'])
		dol_cnt+=1
	min_wage=min(wage_result)
	max_wage=max(wage_result)
	averg=wage_sum//len(wage_result)
	print('MIN__',min_wage,',','MAX__',max_wage,',','AVERG__',averg)
		
 

    

def otbor(arr, csvf):
	sorted(csvf)
	main_key=arr[0]
	
if __name__ == "__main__":
	csv_dict_reader()
	
	
import os
import csv
import re

def write_csv(data, file_name):
	fieldnames = ['post']
	with open(file_name, 'a', newline='', encoding='utf-8-sig') as f:
		#print(data)
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
			profs={'post':(line['name'])
					}
			arr.append(profs)
	write_csv(arr, 'ujasss.csv')
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
		print(prof,' ',' ',count,' ','MIN__',min_wage,',','MAX__',max_wage,',','AVERG__',averg)
		pivot_table={'id':(dol['id']),
					'prof':(vacant_full),
					'count':(count),
					'min_wage':(min_wage),
					'max_wage':(max_wage),
					'average':(averg)
					}
		print(pivot_table)
		pivot_result.append(pivot_table)
	except Exception as e:
		print(e.__class__)
	
	#print(profs_target)
	write_csv(prof_result, 'gruzch_moscow_obl_6_2019.csv')
	write_csv2(pivot_result, vac_file_name+'.csv')
	#return profs

		
def main():
	curDir=os.getcwd()
	files = os.listdir(curDir+"\\data")
	#print(files)
	for file in files:
		this_file=(curDir+"\\data"+"\\"+file)
		csv_dict_reader(this_file)
	



	
if __name__ == "__main__":
	main()
	
	
	
	
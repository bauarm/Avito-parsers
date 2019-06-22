import csv
import re


#otbor_taxist=['водитель','водитель яндекс','водитель uber','водитель такси','таксист'] # по нулевому индекс идет первомоночальный отбор
otbor_taxist=['водител']


 
def csv_dict_reader():
	arr=[]
	arr_wage=[]
	with open('kaluga&obl_vakant_21_6_2019__23_28.csv', mode='r', newline="", encoding='utf-8-sig') as f_obj:
		reader = csv.DictReader(f_obj, delimiter=',')
		
		for line in reader:
			#print(line)
			profs=(line['name'])
			wages=(line['wage'])
			arr.append(profs)
			arr_wage.append(wages)
	dol_cnt=0
	employ=''
	for dol in arr:
		result = re.search(r'водител', str(dol))
		if type(result) == re.Match:
			print(result.string,',',arr_wage[dol_cnt])
		dol_cnt+=1
 

    

def otbor(arr, csvf):
	sorted(csvf)
	main_key=arr[0]
	
if __name__ == "__main__":
	csv_dict_reader()
	
	
import csv
import datetime

def csv_dict_reader():
	arr=[]
	arr_wage=[]
	with open('ujasss.csv', mode='r', newline="", encoding='utf-8-sig') as f_obj:
		reader = csv.DictReader(f_obj, delimiter=',')
		for line in reader:
			#print(line)

			arr.append(line['name'])
	print(arr)
	return arr


def write_csv(data):
	today=datetime.date.today()
	file_name= str("{}_{}_{}_word_count2".format(today.day, today.month, today.year)) + '.csv'
	#print(file_name)
	with open(file_name, 'a', newline='') as f:
		writer = csv.writer(f)
		writer.writerow((data['word'],
                         data['count']
                         ))


def cutter_letter():
	with open('taxi_mos.', 'r', encoding='utf-8-sig') as myfile: 
		data = myfile.read().replace(' ', '').replace(',', '').replace('.', '').lower()
	arr=list(data)
	print(arr)
	return arr
	
def cutter_words():
	
	unnecessary_sign=['«','»',',','.',':',';','—','\ufeff', '\u2009','0xd0', '0xe2','\n','(',')','']
	"""
	with open('prof_kaluga.txt', 'r',  encoding='utf-8-sig') as myfile: 
		data = myfile.read()
	"""
	arr=csv_dict_reader()
	arr_trash=[]
	for item in arr:
		if item in unnecessary_sign:
			arr.remove(item)
			arr_trash.append(item)
		else:
			continue
	myString = ''.join(arr)
	arr_words = myString.split(' ')
	for word in arr_words:
		if len(word)<4:
			arr_words.remove(word)
		else:
			continue
	#print(arr_words)
	return sorted(arr_words)

def word_keeper():
	i=-1
	q=1
	arr=cutter_words()
	#print(arr)
	arr_counter=[]
	arr_reword=[]
	for word in arr:
		i+=1
		if word==arr[i-1]:
			q+=1
		else:
			data = {'word': arr[i-1],
					'count': q
					}
			write_csv(data)
			q=1
			continue
	print(arr_counter)
	

def main():
	
	word_keeper()

if __name__ == "__main__":
	main()
import csv
import datetime




def write_csv(data):
	today=datetime.date.today()
	file_name= str("{}_{}_{}_word_count2".format(today.day, today.month, today.year)) + '.csv'
	#print(file_name)
	with open(file_name, 'a', newline='', encoding='utf-8-sig') as f:
		writer = csv.writer(f)
		writer.writerow((data['word'],
                         data['count']
                         ))

def csv_reader():
	arr=[]
	with open('ujasss.csv', mode='r', newline="", encoding='utf-8-sig') as f_obj:
		reader = csv.DictReader(f_obj, delimiter=',')
		for line in reader:
			#print(line)
			arr.append(line['vakancy'])
	#print(arr)
	return ' '.join(arr)

	
def cutter_words():
	arr=csv_reader()
	w_arr=[]
	#print(len(arr))
	unnecessary_sign=['«','»',',','.',':',';','—','\ufeff', '\u2009','(',')','+','/','"']
	for item in arr:
		#print(item)
		if item in unnecessary_sign:
			continue
		else:
			w_arr.append(item)
	
	
	#print(len(arr))
	myString = ''.join(w_arr)
	#print(myString)
	arr_words = myString.split(' ')
	for word in arr_words:
		#print(len(word))
		if len(word)<4:
			arr_words.remove(word)
			arr_words.append(' ')
			print(word)
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
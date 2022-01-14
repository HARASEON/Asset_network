import requests,bs4 
from bs4 import BeautifulSoup
from pprint import pprint
import pandas as pd
import os
import pickle


def main():
	dataset1 = pd.read_csv('./NASDAQ.csv')
	dataset2 = pd.read_csv('./NYSE.csv')
	data1 = pd.DataFrame(dataset1)
	data2 = pd.DataFrame(dataset2)
	insert_1 = data1[['Symbol']]
	insert_2 = data2[['Symbol']]
	#print(str(insert_1[:1]))
	#print(insert_2)
	#print(data1.loc[0, 'Symbol'])


# Combine insert_1 and insert_2
	data = pd.merge(insert_1, insert_2, on = "Symbol", how="outer")
	a = pd.set_option('display.max_columns', None) # see the all column
	b = pd.set_option('display.max_row', None) # see the all row
	print(b)
	print(data)

	for i in range(len(data1)):
		share_name = list()
		stake = list()
		share_owned = list()
	
		cnt = 0
	
		text = data1.loc[i, 'Symbol']
		url = "https://money.cnn.com/quote/shareholders/shareholders.html?symb="+str(text)+"&subView=institutional" 
	
		rst = requests.get(url)
		print(rst.status_code, url)
	
		html = rst.content
		soup = bs4.BeautifulSoup(html, 'html.parser')
		target = soup.find('table', {'class': 'wsod_dataTable wsod_dataTableBig wsod_institutionalTop10'})
		try: 
			aa = target.select("td.wsod_bold.wsod_grey")
			bb = target.select("td:nth-child(2)")
			cc = target.select("td:nth-child(3)")
	
			for a in aa:
				share_name.append(a.text)
			for b in bb:
				#if cnt > 7:
				stake.append(b.text)
				#cnt = cnt + 1
	
			stake_new = stake[-20:]
	
			print(len(stake_new))
	
			for c in cc:
				share_owned.append(c.text)
	
			final = dict(zip(share_name, stake_new))
	
			print(final)
			
			file_name = "data/" + str(text)
			open(file_name, 'w').write(str(final))	
	
		except Exception as e:
			print(e)
			print('[PASS] {}'.format(text))

	


if __name__== "__main__":
	main()

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

	# print(str(insert_1[:1]))
	# print(insert_2)
	# print(data1.loc[0, 'Symbol'])


# Combine insert_1 and insert_2
# data=pd.merge(insert_1, insert_2, on = "Symbol", how="outer")
# Start again from the last column
	import pdb
	pdb.set_trace()
	df=data2[2179:]
# Scrapping the web information
	for i in range(0,len(df)+1):
		print("geras")

main()


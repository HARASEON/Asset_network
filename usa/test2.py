import requests,bs4 
from bs4 import BeautifulSoup
from pprint import pprint
import pandas as pd

def main():
	dataset1 = pd.read_csv('./NASDAQ.csv')
 	dataset2 = pd.read_csv('./NYSE.csv')
	data1 = pd.DataFrame(dataset1)
	data2 = pd.DataFrame(dataset2)
	insert_1 = data1[['Symbol']]
	insert_2 = data2[['Symbol']]


	for i in range(len(data1)):
		share_name = list()
		stake = list()
		share_owned = list()


		text = data.loc[i, 'Symbol']
		url = "https://money.cnn.com/quote/shareholders/shareholders.html?symb="+str(text)+"&subView=institutional" 

		rst = requests.get(url)
		print(rst.status_code, url)

		html = requests.get(url).content
		soup = bs4.BeautifulSoup(html, 'html.parser')
		target = soup.find('table', {'class': 'wsod_dataTable wsod_dataTableBig wsod_institutionalTop10'})
		try:
			aa = soup.select("td.wsod_bold.wsod_grey")
			bb = soup.select("td:nth-child(2)")
			#bb = soup.find_all("td", id = "wsod_shareholders")	
			cc = soup.select("td:nth-child(3)")

			for a in aa:
				share_name.append(a.text)
			for b in bb:
				stake.append(b.text)
			
			stake_new = stake[-20:]

			print(len(stake_new))

			for c in cc:
				share_owned.append(c.text)

			final = dict(zip(share_name, stake_new))

			print(final)

		except Exception as e:
			print('[PASS] {}'.format(text))




if __name__== "__main__":
	main()

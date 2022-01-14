import csv
import pandas as pd
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time


path = "/home/hr/경제안보/share_miner/chromedriver"

def main():
#	url = 'https://www.barrons.com/market-data/api/proxy?https://quote-barrons.millstone.mktw.dowjones.io/api/quote/overview?chartingSymbol=stock///'
#	path = "/home/hr/경제안보/share_miner/chromdriver"
#	driver = webdriver.Chrome(path)
#	driver.get("https://www.barrons.com/market-data/stocks/{}")

	# {} needs into tickersymbol from csv file(nsye, nasdaq)
	#	print(driver.title) #title
	
	dataset1 = pd.read_csv('./NASDAQ.csv')
	dataset2 = pd.read_csv('./NYSE.csv')
	data1 = pd.DataFrame(dataset1)
	data2 = pd.DataFrame(dataset2)
	insert_1 = data1[['Symbol']]
	insert_2 = data2[['Symbol']]
	print(insert_1)
	print(insert_2)
	
	# Combine insert_1 and insert_2
	data=pd.merge(insert_1, insert_2, on = "Symbol", how="outer")
	print(data)
	
	for i in range(len(data)):
		url = 'https://www.barrons.com/market-data/api/proxy?https://quote-barrons.millstone.mktw.dowjones.io/api/quote/overview?chartingSymbol=stock///'
		driver = webdriver.Chrome(path)
		text = data.loc[i,'Symbol']
		driver.get("https://www.barrons.com/market-data/stocks/" + str(text))
		#driver.get("https://www.barrons.com/market-data/stocks/amzn")

	# clik the value of xpath
		time.sleep(5)
		#driver.find_elements_by_xpath('//*[@id="__next"]/div/div/div[3]/div[8]/div[2]/button')
		#time.sleep(5)

		#driver.find_element_by_xpath('//*[@id="__next"]/div/div/div[3]/div[8]/div[3]/button').click()
		#time.sleep(5) 

		institutional_name = driver.find_elements_by_class_name("Table__Cell-sc-1gtjz8h-2 iZXCTn")
		institutional_shareheld = driver.find_elements_by_class_name("Table__Cell-sc-1gtjz8h-2 isXEvR")
		institutional_percentage = driver.find_elements_by_class_name("Table__Cell-sc-1gtjz8h-2 isXEvR")

		print(institutional_name)


if __name__ == "__main__":
	main()

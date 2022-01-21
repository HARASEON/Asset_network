import json
import codecs
import os


def parser_company(name):
    content = open("data/{}".format(name), 'r', encoding = 'utf-8-sig')
    json_data = json.load(content)['comp'] # comp에 해당하는 value값 불러오기
    for e in json_data:
        print("name:{} share_rate:{}".format(e['SHER_NM'], e['SHER_RT']))

if __name__ == "__main__":
    company_list = os.listdir("data") 
    for c in company_list:
        print("company name",c)
        parser_company(c)

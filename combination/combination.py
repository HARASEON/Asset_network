import pandas as pd
import json
import requests, bs4
import os
from pprint import pprint
from bs4 import BeautifulSoup
import itertools
import networkx as nx
import re


# node : holder, company
# vertex : weight(ratio)

# korea
# to display what we do 

def kor_parser(company):
  content = open("data_korea/{}".format(company), 'r', encoding = 'utf-8-sig')
  json_data = json.load(content)['comp'] # json into dic 

  # comp에 해당하는 value값 불러오기
  for e in json_data:
  # print("name:{} share_rate:{}".format(e['SHER_NM'], e['SHER_RT']))
    holder = e['SHER_NM']
    ratio = e['SHER_RT']

    edges.append((holder, company, {'weight': ratio}))

def us_parser(filename):
  company = filename.split('/')[1]

  data = open(filename).read()
  data = data[1:-1]
  data = data.replace("'" ,'')
  data = data.replace(", ", "")
  reg_exp = re.compile(r"(.*?):(.*?)%")
  match = reg_exp.findall(data)

  for k in match:
    pprint(k)
    if k[0][0]=="," and k[0][1]:
      holder = k[0][2:]
    else:
      holder = k[0]
    ratio = float(k[1])
    edges.append((holder, company, {'weight': ratio}))


if __name__ == "__main__":
  # kor_parsing
  clist = os.listdir("data_korea") # dict into list # korea company list
  company = clist
  edges = []

  # edge generation
  for c in clist:
    try:
      kor_parser(c)
    except:
      print("error in ", c)

  # us_parsing
  files = os.listdir("data_usa")
  filenames = [os.path.join("data_usa", f) for f in files]
  print(filenames)

  # edge generation
  for fn in filenames:
    if fn[-3:] =="swp":
      continue
    try:
      us_parser(fn)
    except:
      print(edges)

  G = nx.DiGraph()
  G.add_edges_from(edges)
  nx.write_gexf(G, "combin.gexf")
  nx.draw_networkx(G)
  plt.show()

  count = {}
  for i in edges:
    try: count [i] += 1
    except: count[i] =1
  print(count)

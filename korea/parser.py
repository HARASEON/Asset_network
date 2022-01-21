import pandas as pd
import json
import requests, bs4
import os
from pprint import pprint
from bs4 import BeautifulSoup
import itertools
import networkx as nx

# node : holder, company
# vertex : weight(ratio)

# korea
# to display what we do 

def kor_parser(company):
  """
  """
  content = open("data_korea/{}".format(company), 'r', encoding = 'utf-8-sig')
  json_data = json.load(content)['comp'] # json into dic 

  # comp에 해당하는 value값 불러오기
  for e in json_data:
  # print("name:{} share_rate:{}".format(e['SHER_NM'], e['SHER_RT']))
    holder = e['SHER_NM']
    ratio = e['SHER_RT']

    edges.append((holder, company, {'weight': ratio}))



if __name__ == "__main__":
  print("hr")

  # to display what we do
  clist = os.listdir("data_korea") # dict into list # korea company list
  company = clist
  edges = []
  for c in clist:
    try:
      kor_parser(c)
    except:
      print("error in ", c)

  G = nx.DiGraph()
  G.add_edges_from(edges)
  nx.write_gexf(G, "korea.gexf")


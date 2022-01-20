import os
import networkx as nx
import json
import matplotlib.pyplot as plt
from pprint import pprint
import re
import codecs # encoder & decoder(txt2byte, txt2txt, byte2byte) 

# KOREA parser
def parser_list(company_list):
  reg_exp = re.compile("{(.*?)}")
  match = reg_exp.findall(company_list)

  reg_exp = re.compile("\"(.*?)\"")
  data = [[reg_exp.findall(p)[0], reg_exp.findall(p)[3]] for p in match]

  content = open("data_korea/{}".format(name), 'r', encoding = 'utf-8-sig')
  json_data = json.load(content)['comp'] # comp에 해당하는 value값 불러오기

  for e in json_data:
    print("name:{} share_rate:{}".format(e['SHER_NM'], e['SHER_RT_SUM']))
    holder = e['SHER_NM']
    ratio = e['SHER_RT_SUM']
    print(holder)
    print(ratio)
  edges.append((holder, company, {'weight': ratio}))

# USA parser
def data_parser(filename):
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
  print("hr")

# KOREA
  files_1 = os.listdir("data_korea")
  filenames_1 = [os.path.join("data_korea",f) for d in files_1[:100]]
  compay_lists = os.listdir("data_korea")
  print(company_lists)
  for c in company_list:
    parser_company(c)
  company_list = open("company_list.txt").read()
  dk=parser_list(company_list)
  print(dk)

# USA
  files = os.listdir("data_usa")

  filenames = [os.path.join("data_usa", f) for f in files][:100]
  #filenames = [os.path.join("data", f) for f in files]
  print(filenames)

  edges = []

  # edge generation

  for ds in filesnames_1:
    if ds[-3:] == "swp":
      continue
    try:
      data_parser(ds)
    except:
      print(edges)

  for fn in filenames:
    if fn[-3:] =="swp":
      continue
    try:
      data_parser(fn)
    except:
      print(edges)

  G = nx.DiGraph()
  G.add_edges_from(edges) # adding list into edge

  nx.write_gexf(G, "data_combin.gexf")
  nx.draw_networkx(G)
  plt.show()

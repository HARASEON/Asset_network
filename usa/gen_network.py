import os
import networkx as nx
import json
import matplotlib.pyplot as plt

import re

def data_parser(filename):
    company = filename.split('/')[1]

    data = open(filename).read()

    data = data[1:-1]
    data = data.replace("'" ,'')
    reg_exp = re.compile(r"(.*?):(.*?)%")
    match = reg_exp.findall(data)
    
    for k in match:
        if k[0][0]=="," and k[0][1]:
            holder = k[0][2:]
        else:
            holder = k[0]

        ratio = float(k[1])
        edges.append((holder, company, {'weight': ratio}))



if __name__ == "__main__":
    print("graycat")

    files = os.listdir("data")

    filenames = [os.path.join("data", f) for f in files][:100]
    print(filenames)

    edges = []

    #edge generation
    for fn in filenames:
        if fn[-3:] =="swp":
            continue
        try:
            data_parser(fn)
        except:
            import pdb
            pdb.set_trace()

    G = nx.DiGraph()
    G.add_edges_from(edges)

    nx.write_gexf(G, "data.gexf")
    nx.draw_networkx(G)
    plt.show()


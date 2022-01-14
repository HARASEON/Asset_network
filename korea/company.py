from urllib.request import urlopen, Request
import re
import os

def get_share_html(company_num):
    """
    Attribute:
        Static web page crawling & parsing
        
    Arguments:
        Company_num
    """
    url = "http://comp.fnguide.com/SVO2/json/data/01_09_01/{}.json".format(company_num)
    try:
        req = Request(url,headers={'User-Agent': 'Mozilla/5.0'})
        html_text = urlopen(req).read()
        # Calling http and scrapping the url and User browser information
        # the User-agent file who are communicating with web server 'Mozilla 5.0'

    except AttributeError as e :
        return None
    return html_text

if __name__=="__main__":
    company_list = open("company_list.txt").read()

    reg_exp = re.compile("\"cd\":\"(.*?)\",.\".*?\":\"(.*?)\"")
    match = reg_exp.findall(company_list)
    coms = []
    #print(match)
    if not os.path.exists("data"):
        os.makedirs("data")

    for m in match:
        try:
            print(m)
            data = get_share_html(m[0]).decode('utf-8')
            open("data/{}".format(m[1]), 'w').write(data)
        except:
            continue

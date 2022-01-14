import re

def parser_list(company_list):
    reg_exp = re.compile("{(.*?)}")
    match = reg_exp.findall(company_list)

    reg_exp = re.compile("\"(.*?)\"")

    data = [[reg_exp.findall(p)[0], reg_exp.findall(p)[3]] for p in match]
    import pdb
    pdb.set_trace()
    return data

def find_company(company_list, name):
    if len(name) >5:
        name = name[:4]
    reg_exp = re.compile("{(.*?)" +name +"(.*?)}")
    match = reg_exp.findall(company_list)

    if match:
        reg_exp = re.compile("\"cd\":\"(.*?)\"")
        match = reg_exp.findall(match[0][0])
        return match[0]
    else:
        return False

if __name__=="__main__":
    company_list = open("company_list.txt").read()
    find_company(company_list, "삼성생총")
    print(company_list)

def get_kwd(txt):
    txt = txt.replace(" ",',')
    txt = txt.replace(",,",',')
    txt = txt.split("\n")
    rows=[]
    dic={}
    for i in txt:
        row = i.split(",")
        rows.append(row)
    for ii in rows:
        for key in ii:
            if key in dic:
                dic[key] = dic[key] + 1
            else:
                dic[key] = 1
    #Only print the maximum value.
    HighValue=0
    HighKey=None
    for key in dic:
        #print(HighKey)
        if dic[key]>HighValue:
            #print(HighKey)
            if str(key).isalpha() & (not key in ['', 'to','the', 'be', 'should', 'is', 'that',
                                                'able', 'of', 'a', 'and', 'or', 'from', 'in', 'for', 'on']):
                HighValue=dic[key]
                HighKey=key
        if HighKey == None:
            HighKey = txt[0]
    return HighKey

def find_keyword(txt):
    "Find keyword which pargraghs it's in"
    keyword = get_kwd(txt)
    txt = txt.replace(" ", ',')
    txt = txt.replace(",,", ',')
    txt = txt.split("\n")
    para_dict = {}
    para_num = 1
    for para in txt:
        if para != '':
            words = para.split(",")
            para_key = False
            if keyword in words:
                para_key = True
            para_dict[para_num] = para_key
            para_num = para_num + 1
    para_list = ''
    i = 0
    for i in range(len(para_dict)):
        if para_dict[i + 1] == True:
            para_list += str(i + 1)
            if i > 0 and i is not len(para_dict) - 1:
                para_list += ', '
    para_list = para_list[0:-2]
    
    return para_list

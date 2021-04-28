from nltk.util import re_show
from rake_nltk import Rake

r = Rake()
# def get_kwd(my_text):

#     r.extract_keywords_from_text(my_text)
#     res_scores = r.get_ranked_phrases_with_scores()
#     if len(res_scores) < 1:
#         return ''
#     res = res_scores[0][1]  #get keyword phrases ranked highest
#     return res
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
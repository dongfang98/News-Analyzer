from nltk.util import re_show
from rake_nltk import Rake

r = Rake()
def get_kwd(my_text):

    r.extract_keywords_from_text(my_text)
    res_scores = r.get_ranked_phrases_with_scores()
    if len(res_scores) < 1:
        return ''
    res = res_scores[0][1]  #get keyword phrases ranked highest
    return res

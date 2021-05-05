import nltk
nltk.download('stopwords')
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import sent_tokenize


def get_sen(text):
    
    view = []
    for i in sent_tokenize(text.replace('\n','')):
        view.append(i)


    sid = SentimentIntensityAnalyzer()
    sentiment_val = 0
    for each in view:
        ss = sid.polarity_scores(each)
        sentiment_val += ss['compound'] * len(each)
    if sentiment_val > 0:
        return 'Positive'
    elif sentiment_val == 0:
        return 'Neutral'
    else:
        return 'Negative'

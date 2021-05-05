from newsapi import NewsApiClient

api = NewsApiClient(api_key='3c394f2eecf146eab191192d3702002f')

def get_all(keyword, number):
    all_articles = api.get_everything(q=keyword, page_size=number)
    return all_articles


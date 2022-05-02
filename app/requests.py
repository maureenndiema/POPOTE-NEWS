import urllib.request,json #helps create a connection to our API URL and send a request, formats the JSON response to a Python dictionary
from .models import Sources,Articles,Keyword,Breaking

api_Key= None
base_url= None
top_articles_url= None
keyword_url= None
breaking_news_url= None

def configure_request(app):
    global api_Key, base_url, top_articles_url, keyword_url, breaking_news_url
    api_Key = app.config['NEWS_API_KEY']
    base_url = app.config["NEWS_API_BASE_URL"]
    top_articles_url = app.config["NEWS_API_TOP_ARTICLES_BASE_URL"]
    keyword_url = app.config["NEWS_API_SEARCH_KEYWORD_BASE_URL"]
    breaking_news_url = app.config["NEWS_API_BREAKING_NEWS_BASE_URL"]


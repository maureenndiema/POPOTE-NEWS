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

def get_sources():
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = base_url.format(api_Key) #construct the news api url

    with urllib.request.urlopen(get_sources_url) as url: #sending request as url
        get_sources_data = url.read() #reading the response and storing in a get_sources_data variable
        get_sources_response = json.loads(get_sources_data) #converting the JSON response to a Python dictionary

        sources_results = None

        if get_sources_response['sources']: #checking if response has any data
            sources_results_list = get_sources_response['sources']
            sources_results = process_sources(sources_results_list)  

    return sources_results #return a list of sources objects

def process_sources(sources_list):
    '''
    Function  that processes the sources result and transform them to a list of Objects
    Args:
        sources_list: A list of dictionaries that contain sources details
    Returns :
        sources_results: A list of sources objects
    '''
    sources_results = [] #to store our newly created sources objects
    for sources_item in sources_list:
        id = sources_item.get('id')
        name = sources_item.get('name')
        description = sources_item.get('description')
        url = sources_item.get('url')
        category = sources_item.get('category')
        language = sources_item.get('language')

        sources_object = Sources(id, name, description, url, category, language)
        sources_results.append(sources_object)
    return sources_results

def get_top_articles(id):
    '''
    Function that gets the json response to our url request
    '''
    get_articles_url = top_articles_url.format(id, api_Key) #construct the top articles api url

    with urllib.request.urlopen(get_articles_url) as url: #sending request as url
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_results = None

        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = process_articles(articles_results_list)
    
    return articles_results

def process_articles(articles_list):
    articles_results = []
    for articles_item in articles_list:
        author = articles_item.get('author')
        title = articles_item.get('title')
        imageurl = articles_item.get('urlToImage')
        publishedOn = articles_item.get('publishedAt')
        publishedAt = date_convert(publishedOn)
        url = articles_item.get('url')

        if imageurl:
            articles_object = Articles(author,title,imageurl,publishedAt,url)
            articles_results.append(articles_object)
    return articles_results


    
    



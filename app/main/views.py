from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_sources, get_top_articles,get_keyword, get_breaking_news

# Views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    #Getting sources
    sources = get_sources()
    breaking_news = get_breaking_news()
    title = 'The Daily Telegram'
    get_keyword = request.args.get('keyword_query')

    if get_keyword:
        return redirect(url_for('main.keyword', keyword_name=get_keyword))
    else:
        return render_template('index.html', title = title, sources=sources, breaking_news=breaking_news)
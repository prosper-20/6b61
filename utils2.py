import requests
from decouple import config
from news.models import News
url = f"https://newsdata.io/api/1/news?apikey={config('API_KEY')}&q=pegasus&language=en"

all_my_news = []

def generate_news(url):
    response = requests.get(url)
    all_news = dict(response.json())
    for news in all_news['results']:
        headline = news.get("title")
        content = news.get("content")
        category = news.get("category")
        link = news.get("link")
        video_link = news.get("video_link")
        reporter = news.get("creator")
        image = news.get("image_url")
        date_posted = news.get("pubDate")
        all_my_news.append(news)

        News.objects.create(headline=headline, content=content, category=category, link=link,
                            video_link=video_link, reporter=reporter, image=image, 
                            date_posted=date_posted)

    return("Confirm!!")







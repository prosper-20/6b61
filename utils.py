from decouple import config
import requests
from news.models import News
url = f"https://newsdata.io/api/1/news?apikey={config('API_KEY')}&q=pegasus&language=en"

headlines = []

def generate_news(url):
    response = requests.get(url)

    dictionary_form = dict(response.json())

    all_news = dictionary_form.get("results")

    for news in all_news:
        headlines.append(news.get("headline"))
        print(news.get("headline"))
    return headlines
    

#     for news in all_news:
#         headline = news.get("title")
#         content = news.get("content")
#         category = news.get("category")
#         link = news.get("link")
#         video_link = news.get("video_link")
#         reporter = news.get("creator")
#         image = news.get("image_url")
#         date_posted = news.get("pubDate")

#         News.objects.create(headline=headline, content=content, category=category, link=link,
#                             video_link=video_link, reporter=reporter, image=image, 
#                             date_posted=date_posted)
        
#     return("News has been created, check your admin")

# print(generate_news(url))
    










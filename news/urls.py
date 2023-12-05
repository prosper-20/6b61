from django.urls import path
from .views import NewsHomePage, NewsDetailPage, generate_news_view

urlpatterns =[
    path("all/", NewsHomePage.as_view(), name="all-news"),
    path("generate/", generate_news_view, name="generate-news"),
    path("<int:id>/", NewsDetailPage.as_view(), name="detail")


]
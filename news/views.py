from django.shortcuts import render
from rest_framework.response import Response
from .serializers import NewsSerializer
from .models import News
from rest_framework.views import APIView
from rest_framework import status
from utils2 import generate_news
from django.http import HttpResponse
from decouple import config


def generate_news_view(request):
    url = f"https://newsdata.io/api/1/news?apikey={config('API_KEY')}&q=pegasus&language=en"
    generate_news(url)
    return HttpResponse("News generated")

class NewsHomePage(APIView):
    def get(self, request, format=None, *args, **kwargs):
        all_news = News.objects.all()
        serialized_news = NewsSerializer(all_news, many=True)
        return Response(serialized_news.data, status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
        new_news = NewsSerializer(data=request.data)
        new_news.is_valid(raise_exception=True)
        new_news.save()
        return Response({"Success": "News has been added successfully!"}, 
                        status=status.HTTP_201_CREATED)
    
from django.shortcuts import get_object_or_404

class NewsDetailPage(APIView):
    def get(self, request, id):
        single_news = get_object_or_404(News, id=id)
        serialized_news = NewsSerializer(single_news)
        return Response(serialized_news.data, status=status.HTTP_200_OK)
    
    def put(self, request, id):
        single_news = get_object_or_404(News, id=id)
        serialized_news = NewsSerializer(single_news, data=request.data, partial=True)
        serialized_news.is_valid(raise_exception=True)
        serialized_news.save()
        return Response("Update successful", status=status.HTTP_202_ACCEPTED)
    
    def delete(self, request, id):
        single_news = get_object_or_404(News, id=id)
        single_news.delete()
        return Response("News has been deleted", status=status.HTTP_204_NO_CONTENT)

        
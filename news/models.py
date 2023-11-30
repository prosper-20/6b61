from django.db import models

# Create your models here.

class News(models.Model):
    headline = models.CharField(max_length=200)
    content = models.TextField()
    category = models.CharField()
    reporter = models.CharField(max_length=300)
    image = models.ImageField(upload_to="news_images", blank=True, null=True)
    date_posted = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.headline


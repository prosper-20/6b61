from django.db import models

# Create your models here.

class News(models.Model):
    headline = models.CharField(max_length=200)
    content = models.TextField()
    category = models.CharField(max_length=100)
    link = models.URLField(blank=True, null=True)
    video_link = models.URLField(blank=True, null=True)
    reporter = models.CharField(max_length=300)
    image = models.URLField(blank=True, null=True)
    date_posted = models.CharField(max_length=40)

    class Meta:
        verbose_name_plural = "News"

    def __str__(self):
        return self.headline


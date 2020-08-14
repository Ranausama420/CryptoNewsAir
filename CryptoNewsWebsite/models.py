from django.utils import timezone
from django.contrib import admin
from django.db import models
import json
import psycopg2

# Create your models here.

class newsdata(models.Model):

     idbyapi= models.CharField(max_length=200)
     hotness= models.TextField()
     activityHotness= models.TextField()
     primaryCategory= models.TextField()
     words= models.TextField()
     similarArticles= models.TextField()
     coins= models.TextField()
     description= models.TextField()
     publishedAt= models.TextField()
     title= models.TextField()
     url= models.TextField()
     source= models.TextField()
     sourceDomain= models.TextField()
     originalImageUrl= models.TextField()

     def __str__(self):
          return self.idbyapi

admin.site.register(newsdata)

class topnewsdata(models.Model):

     idbyapi= models.CharField(max_length=200)
     hotness= models.TextField()
     activityHotness= models.TextField()
     primaryCategory= models.TextField()
     words= models.TextField()
     similarArticles= models.TextField()
     coins= models.TextField()
     description= models.TextField()
     publishedAt= models.TextField()
     title= models.TextField()
     url= models.TextField()
     source= models.TextField()
     sourceDomain= models.TextField()
     originalImageUrl= models.TextField()

     def __str__(self):
          return self.idbyapi

admin.site.register(topnewsdata)

class bitcoinnewsdata(models.Model):

     idbyapi= models.CharField(max_length=200)
     hotness= models.TextField()
     activityHotness= models.TextField()
     primaryCategory= models.TextField()
     words= models.TextField()
     similarArticles= models.TextField()
     coins= models.TextField()
     description= models.TextField()
     publishedAt= models.TextField()
     title= models.TextField()
     url= models.TextField()
     source= models.TextField()
     sourceDomain= models.TextField()
     originalImageUrl= models.TextField()

     def __str__(self):
          return self.idbyapi

admin.site.register(bitcoinnewsdata)

class ripplenewsdata(models.Model):

     idbyapi= models.CharField(max_length=200)
     hotness= models.TextField()
     activityHotness= models.TextField()
     primaryCategory= models.TextField()
     words= models.TextField()
     similarArticles= models.TextField()
     coins= models.TextField()
     description= models.TextField()
     publishedAt= models.TextField()
     title= models.TextField()
     url= models.TextField()
     source= models.TextField()
     sourceDomain= models.TextField()
     originalImageUrl= models.TextField()

     def __str__(self):
          return self.idbyapi

admin.site.register(ripplenewsdata)

class ethereumnewsdata(models.Model):

     idbyapi= models.CharField(max_length=200)
     hotness= models.TextField()
     activityHotness= models.TextField()
     primaryCategory= models.TextField()
     words= models.TextField()
     similarArticles= models.TextField()
     coins= models.TextField()
     description= models.TextField()
     publishedAt= models.TextField()
     title= models.TextField()
     url= models.TextField()
     source= models.TextField()
     sourceDomain= models.TextField()
     originalImageUrl= models.TextField()

     def __str__(self):
          return self.idbyapi

admin.site.register(ethereumnewsdata)
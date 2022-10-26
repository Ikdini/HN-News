from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework import response, status
import http.client
import json
from .models import *
from . import tasks


# Create your views here.


def baseAPIConnection(url):
  conn = http.client.HTTPSConnection("hacker-news.firebaseio.com")
  payload = "{}"
  conn.request("GET", url, payload)
  res = conn.getresponse()
  data = res.read()
  return json.loads(data.decode("utf-8"))


class MaxItemView(GenericAPIView):
  def get(self, request):
    # Get the max item id from the API
    url = "/v0/maxitem.json?print=pretty"
    decoded = baseAPIConnection(url)
    # tasks.sync_stories_task.delay()
    return response.Response({'Max Item Id': decoded}, status=status.HTTP_200_OK)


class GetItemView(GenericAPIView):

  def get(self, request):
    # get all items from the database and return them
    def mySort(item):
      return item['time']

    stories = [story.serialize() for story in Story.objects.all()]
    jobs = [job.serialize() for job in Job.objects.all()]

    items = stories + jobs
    items.sort(key=mySort, reverse=True)
    return response.Response(items, status=status.HTTP_200_OK)

  # def get(self, request):
  #   # TODO: add a try catch block to handle the error
  #   # Get new stories from the API

  #   url = "/v0/newstories.json?print=pretty"
  #   decoded = baseAPIConnection(url)
  #   decoded_100 = decoded[:100]

  #   # get the item properties and save to the database if it doesn't exist
  #   for itemId in decoded_100:
  #     if Story.objects.filter(id=itemId).exists():
  #       print(f'Story already exists with id {itemId}')
  #       continue

  #     url = f"/v0/item/{itemId}.json?print=pretty"
  #     decoded_dtls = baseAPIConnection(url)

  #     try:
  #       if 'deleted' in decoded_dtls:
  #         continue
  #     except Exception as e:
  #       print(e)
  #       print(
  #           f'ERROR OCCURED WITH THIS ID {itemId} WHEN CHECKING IF DELETED\n')
  #       continue

  #     id = decoded_dtls['id']
  #     typ = decoded_dtls['type']
  #     by = None
  #     time = None
  #     descendants = None
  #     score = None
  #     title = None
  #     url = "http://stoplight.io/prism/"

  #     try:
  #       if "by" in decoded_dtls:
  #         by = decoded_dtls["by"]
  #       if "time" in decoded_dtls:
  #         time = decoded_dtls["time"]
  #       if "descendants" in decoded_dtls:
  #         descendants = decoded_dtls["descendants"]
  #       if "score" in decoded_dtls:
  #         score = decoded_dtls["score"]
  #       if "title" in decoded_dtls:
  #         title = decoded_dtls["title"]
  #       if "url" in decoded_dtls:
  #         url = decoded_dtls["url"]
  #     except Exception as e:
  #       print(e)
  #       print(
  #           f'ERROR OCCURED WITH THIS ID {itemId} WHEN CHECKING THE DECODED PROPERTIES\n')
  #       print(f'{decoded_dtls}\n')
  #       continue

  #     Story.objects.create(id=id, type=typ, by=by, time=time,
  #                          descendants=descendants, score=score, title=title, url=url)

  #   # delete the old stories from the database
  #   # TODO: edit this lines
  #   print(Story.objects.all().count())
  #   if Story.objects.all().count() > 100:
  #     all_stories = Story.objects.all()
  #     old_stories = all_stories[100:]
  #     print(old_stories.count())
  #     for story in old_stories:
  #       story.delete()
  #   print(Story.objects.all().count())

  #   items = [story.serialize() for story in Story.objects.all()]

  #   return response.Response(items, status=status.HTTP_200_OK)


class NewStoriesView(GenericAPIView):
  def get(self, request):
    # Get the latest 100 stories Id from the API
    url = "/v0/newstories.json?print=pretty"
    decoded = baseAPIConnection(url)
    decoded_100 = decoded[:100]
    return response.Response({'New Stories Id': decoded_100}, status=status.HTTP_200_OK)


class NewJobsView(GenericAPIView):
  def get(self, request):
    # Get the latest 100 stories Id from the API
    url = "/v0/jobstories.json?print=pretty"
    decoded = baseAPIConnection(url)
    decoded_100 = decoded[:100]
    return response.Response({'New Jobs Id': decoded_100}, status=status.HTTP_200_OK)

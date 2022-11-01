from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework import response, status
import http.client
import json
from .models import *
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import *


# Create your views here.


def baseAPIConnection(url):
  conn = http.client.HTTPSConnection("hacker-news.firebaseio.com")
  payload = "{}"
  conn.request("GET", url, payload)
  res = conn.getresponse()
  data = res.read()
  return json.loads(data.decode("utf-8"))


def pagination(self, request, items):
  pg = request.query_params.get('page')
  if pg:
    page = self.paginate_queryset(items)
    if page is not None:
      return page, pg


class MaxItemIdView(GenericAPIView):
  def get(self, request):
    # Get the max item id from the API
    url = "/v0/maxitem.json?print=pretty"
    decoded = baseAPIConnection(url)
    return response.Response({'Max Item Id': decoded}, status=status.HTTP_200_OK)


class NewStoriesView(GenericAPIView):
  def get(self, request):
    # Get the latest 100 stories Id from the API
    url = "/v0/newstories.json?print=pretty"
    decoded_100 = baseAPIConnection(url)[:100]

    # pagination
    if pagination(self, request, decoded_100):
      page, pg = pagination(self, request, decoded_100)  # type: ignore
      return self.get_paginated_response({f'New Stories Id Page {pg}': page})

    return response.Response({'New Stories Id': decoded_100}, status=status.HTTP_200_OK)


class TopStoriesView(GenericAPIView):
  def get(self, request):
    # Get the top 100 stories Id from the API
    url = "/v0/topstories.json?print=pretty"
    decoded_100 = baseAPIConnection(url)[:100]

    # pagination
    if pagination(self, request, decoded_100):
      page, pg = pagination(self, request, decoded_100)  # type: ignore
      return self.get_paginated_response({f'Top Stories Id Page {pg}': page})

    return response.Response({'Top Stories Id': decoded_100}, status=status.HTTP_200_OK)


class LatestJobsView(GenericAPIView):
  def get(self, request):
    # Get the latest 100 jobs Id from the API
    url = "/v0/jobstories.json?print=pretty"
    decoded_100 = baseAPIConnection(url)[:100]

    # pagination
    if pagination(self, request, decoded_100):
      page, pg = pagination(self, request, decoded_100)  # type: ignore
      return self.get_paginated_response({f'Latest Jobs Id Page {pg}': page})

    return response.Response({'Latest Jobs Id': decoded_100}, status=status.HTTP_200_OK)


class GetItemsView(GenericAPIView):

  def get(self, request):

    # filter by type
    type = request.query_params.get('type')
    if type:
      if type == 'story':
        items = Story.objects.all()
        serializer = StorySerializer(items, many=True)
      else:
        items = Job.objects.all()
        serializer = JobSerializer(items, many=True)

      # pagination
      if pagination(self, request, serializer.data):
        page, pg = pagination(self, request, serializer.data)  # type: ignore
        return self.get_paginated_response({f'{type} page {pg}': page})

      return response.Response({f'{type}': serializer.data}, status=status.HTTP_200_OK)

    # get all items from the database and return them
    def mySort(item):
      return item['time']

    serializer1 = StorySerializer(Story.objects.all(), many=True)
    serializer2 = JobSerializer(Job.objects.all(), many=True)
    items = serializer1.data + serializer2.data  # type: ignore
    items.sort(key=mySort, reverse=True)

    # pagination
    if pagination(self, request, items):
      page, pg = pagination(self, request, items)  # type: ignore
      return self.get_paginated_response({f'All Items page {pg}': page})

    return response.Response(items, status=status.HTTP_200_OK)

from .views import *
from django.urls import path

urlpatterns = [
    path('maxitemid', MaxItemIdView.as_view(), name='maxitemid'),
    path('newstories', NewStoriesView.as_view(), name='newstories'),
    path('topstories', TopStoriesView.as_view(), name='topstories'),
    path('latestjobs', LatestJobsView.as_view(), name='latestjobs'),
    path('items', GetItemsView.as_view(), name='items'),
]

from .views import *
from django.urls import path

urlpatterns = [
    path('maxitem', MaxItemView.as_view(), name='maxitem'),
    path('newstories', NewStoriesView.as_view(), name='newstories'),
    path('items', GetItemView.as_view(), name='items'),
]

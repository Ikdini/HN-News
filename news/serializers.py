from rest_framework.serializers import ModelSerializer
from .models import *


class StorySerializer(ModelSerializer):
  class Meta:
    model = Story
    fields = ('id', 'type', 'by', 'time',
              'descendants', 'score', 'title', 'url')


class JobSerializer(ModelSerializer):
  class Meta:
    model = Job
    fields = ('id', 'type', 'by', 'time',
              'text', 'title', 'url')

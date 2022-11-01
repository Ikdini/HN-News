from django.db import models
from helpers.models import BaseModel

# Create your models here.


class Story(BaseModel):
  descendants = models.IntegerField(blank=True, null=True)
  score = models.IntegerField(blank=True, null=True)
  title = models.CharField(max_length=255, blank=True, null=True)
  url = models.URLField(
      default="http://stoplight.io/prism/", blank=True, null=True)

  def __str__(self):
    return f"({self.id}) {self.type} by {self.by} at {self.time}"


class Job(BaseModel):
  text = models.TextField(blank=True, null=True)
  url = models.URLField(blank=True, null=True)
  title = models.CharField(max_length=255, blank=True, null=True)

  def __str__(self):
    return f"({self.id}) {self.type} by {self.by} at {self.time}"

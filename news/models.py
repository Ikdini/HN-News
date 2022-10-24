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
    return f"({self.id}) {self.type} by {self.by}"

  def serialize(self):
    return {
        "id": self.id,
        "type": self.type,
        "by": self.by,
        "time": self.time,
        "descendants": self.descendants,
        "score": self.score,
        "title": self.title,
        "url": self.url,
    }


class Job(BaseModel):
  text = models.TextField(blank=True, null=True)
  url = models.URLField(blank=True, null=True)
  title = models.CharField(max_length=255, blank=True, null=True)

  def __str__(self):
    return f"({self.id}) {self.type} by {self.by}"

  def serialize(self):
    return {
        "id": self.id,
        "type": self.type,
        "by": self.by,
        "time": self.time,
        "text": self.text,
        "url": self.url,
        "title": self.title,
    }


# class Comment(BaseModel):
#   parent = models.IntegerField(blank=True, null=True)
#   text = models.TextField(blank=True, null=True)

#   def __str__(self):
#     return f"({self.id}) {self.type} by {self.by}"


# class Poll(BaseModel):
#   descendants = models.IntegerField(blank=True, null=True)
#   score = models.IntegerField(blank=True, null=True)
#   title = models.CharField(max_length=255, blank=True, null=True)
#   text = models.TextField(blank=True, null=True)

#   def __str__(self):
#     return f"({self.id}) {self.type} by {self.by}"


# class PollOption(BaseModel):
#   parent = models.IntegerField(blank=True, null=True)
#   text = models.TextField(blank=True, null=True)

#   def __str__(self):
#     return f"({self.id}) {self.type} by {self.by}"

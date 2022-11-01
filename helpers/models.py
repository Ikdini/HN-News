from django.db import models


class BaseModel(models.Model):
  items = [
      ('job', 'Job'),
      ('story', 'Story'),
  ]

  id = models.IntegerField(primary_key=True, unique=True)
  deleted = models.BooleanField(default=False, blank=True, null=True)
  type = models.CharField(max_length=10, choices=items)
  by = models.CharField(max_length=100, blank=True, null=True)
  time = models.IntegerField(blank=True, null=True)

  class Meta:
    abstract = True
    ordering = ['-time']

from .models import *
from celery import shared_task
from . import views

# Create your tasks here


@shared_task
def sync_stories_task():
  # TODO: add a try catch block to handle the error
  # Get new stories from the API
  url = "/v0/newstories.json?print=pretty"
  decoded = views.baseAPIConnection(url)
  decoded_100 = decoded[:100]

  # get the item properties and save to the database if it doesn't exist
  for itemId in decoded_100:
    if Story.objects.filter(id=itemId).exists():
      print(f'Story already exists with id {itemId}')
      continue

    url = f"/v0/item/{itemId}.json?print=pretty"
    decoded_dtls = views.baseAPIConnection(url)

    try:
      if 'deleted' in decoded_dtls:
        continue
    except Exception as e:
      print(e)
      print(
          f'ERROR OCCURED WITH THIS ID {itemId} WHEN CHECKING IF DELETED\n')
      continue

    id = decoded_dtls['id']
    typ = decoded_dtls['type']
    by = None
    time = None
    descendants = None
    score = None
    title = None
    url = "http://stoplight.io/prism/"

    try:
      if "by" in decoded_dtls:
        by = decoded_dtls["by"]
      if "time" in decoded_dtls:
        time = decoded_dtls["time"]
      if "descendants" in decoded_dtls:
        descendants = decoded_dtls["descendants"]
      if "score" in decoded_dtls:
        score = decoded_dtls["score"]
      if "title" in decoded_dtls:
        title = decoded_dtls["title"]
      if "url" in decoded_dtls:
        url = decoded_dtls["url"]
    except Exception as e:
      print(e)
      print(
          f'ERROR OCCURED WITH THIS ID {itemId} WHEN CHECKING THE DECODED PROPERTIES\n')
      print(f'{decoded_dtls}\n')
      continue

    Story.objects.create(id=id, type=typ, by=by, time=time,
                         descendants=descendants, score=score, title=title, url=url)

  # delete the old stories from the database
  # TODO: edit this lines
  print(Story.objects.all().count())
  if Story.objects.all().count() > 100:
    all_stories = Story.objects.all()
    old_stories = all_stories[100:]
    print(old_stories.count())
    for story in old_stories:
      story.delete()
  print(Story.objects.all().count())
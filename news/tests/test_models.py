from rest_framework.test import APITestCase
from ..models import *


class TestModel(APITestCase):

  def test_create_job(self):
    new_job = Job.objects.create(id=1, type='job', by='Dini', time=123456789,
                                 text='This is a job', url='http://example.com', title='Job')
    self.assertIsInstance(new_job, Job)
    job = Job.objects.get(id=1)
    self.assertEqual(job.type, 'job')

  def test_create_story(self):
    new_story = Story.objects.create(id=1, type='story', by='Dini', time=123456789,
                                     descendants=1, score=1, title='Story')
    self.assertIsInstance(new_story, Story)
    self.assertEqual(new_story.url, 'http://stoplight.io/prism/')

  def test_create_comment(self):
    new_comment = Comment.objects.create(id=1, type='comment', by='Dini', time=123456789,
                                         parent=1, text='This is a comment')
    self.assertIsInstance(new_comment, Comment)

  def test_create_poll(self):
    new_poll = Poll.objects.create(id=1, type='poll', by='Dini', time=123456789,
                                   descendants=1, score=1, title='Poll', text='This is a poll')
    self.assertIsInstance(new_poll, Poll)

  def test_create_poll_option(self):
    new_poll_option = PollOption.objects.create(id=1, type='pollopt', by='Dini', time=123456789,
                                                parent=1, text='This is a poll option')
    self.assertIsInstance(new_poll_option, PollOption)

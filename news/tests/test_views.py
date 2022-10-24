from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse


def baseAPIConnection(self, name):
  url = reverse(name)
  response = self.client.get(url)
  return response


class TestViews(APITestCase):

  def test_max_item_id_view(self):
    response = baseAPIConnection(self, 'maxitemid')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertIsInstance(response.data, dict)
    self.assertIsInstance(response.data['Max Item Id'], int)

  def test_new_stories_view(self):
    response = baseAPIConnection(self, 'newstories')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertIsInstance(response.data, dict)
    self.assertIsInstance(response.data['New Stories'], list)
    self.assertEqual(len(response.data['New Stories']), 100)

  def test_get_item_view(self):
    response = baseAPIConnection(self, 'items')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertIsInstance(response.data, dict)
    self.assertIsInstance(response.data['id'], int)
    self.assertIsInstance(response.data['type'], str)

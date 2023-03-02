from django.test import SimpleTestCase
from django.urls import reverse, resolve
from activity1.views import registration_view


class TestUrls(SimpleTestCase):

    def test_list_url_is_resolved(self):
        url = reverse('registration')
        print(resolve(url))
        self.assertEquals(resolve(url).func, registration_view)
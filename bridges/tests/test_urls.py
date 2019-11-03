from django.test import SimpleTestCase
from django.urls import reverse, resolve


# from newsapp.views import NewsListView, NewsCreateView, NewsDetailView, NewsDeleteView, NewsUpdateView

from authapp.views import register, restricted_area, user_profile

class TestUrls(SimpleTestCase):

    """docstring for TestUrls SimpleTestCase"""

    """Unittest for newsapp"""

    # def test_news_list_url_is_resolved(self):
    #     url = reverse('news_list')
    #     self.assertEquals(resolve(url).func.view_class, NewsListView)

    # def test_news_create_url_is_resolved(self):
    #     url = reverse('news_create', kwargs={int: 'project_pk'})
    #     self.assertEquals(resolve(url).func.view_class, NewsCreateView)

    # def test_news_detail_url_is_resolved(self):
    #     url = reverse('news_detail', kwargs={'<int:pk>'})
    #     self.assertEquals(resolve(url).func.view_class, NewsDetailView)

    # def test_news_delete_url_is_resolved(self):
    #     url = reverse('news_delete')
    #     self.assertEquals(resolve(url).func.view_class, NewsDeleteView)

    # def test_news_supdate_url_is_resolved(self):
    #     url = reverse('news_supdate', kwargs={'pk':1})
    #     self.assertEquals(resolve(url).func.view_class, NewsUpdateView)

    """Unittest for authapp"""

    def test_register_url_is_resolved(self):
        url = reverse('register')
        self.assertEquals(resolve(url).func, register)

    def test_restricted_area_url_is_resolved(self):
        url = reverse('restricted_area')
        self.assertEquals(resolve(url).func, restricted_area)

    def test_user_profile_url_is_resolved(self):
        url = reverse('user_profile', kwargs={'pk':1})
        self.assertEquals(resolve(url).func, user_profile)

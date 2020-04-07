from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

from lists.views import home_page

class HomePageTest(TestCase):
    
    #def test_root_url_resolve_to_home_page_view(self):
        #found = resolve('/')
        #self.assertEqual(found.func, home_page)

    #def test_home_page_returns_correct_html(self):
        #request = HttpRequest() # (1)
        #response = home_page(request) # (2)
        #response = self.client.get('/') # (1)
        
        #html = response.content.decode('utf8') # (2)
        #self.assertTrue(html.startswith('<html>'))
        #self.assertIn('<title>TO-DO lists</title>',html)
        #self.assertTrue(html.endswith('</html>'))

        #self.assertTemplateUsed(response, 'home.html') # (3)
        #expected_html = render_to_string('home.html')
        #self.assertEqual(html, expected_html)

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
        

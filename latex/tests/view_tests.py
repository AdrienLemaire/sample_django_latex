# from django
from django.test import TestCase
from django.core.urlresolvers import reverse


class LatexViewTest(TestCase):
    """Testing views"""

    def test_home(self):
        "Verify if we get the home page"
        url = reverse("latex:home")
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        self.assertContains(response, reverse("latex:get_pdf"))

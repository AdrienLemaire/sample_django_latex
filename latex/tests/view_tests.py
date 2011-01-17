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

    def test_get_pdf(self):
        "Verify that we get a pdf"
        # Basic test
        url = reverse("latex:get_pdf")
        response = self.client.post(url)
        self.assertEqual('application/pdf', response['Content-Type'])
        # Default filename = "test"
        self.assertTrue("test" in response['Content-Disposition'])

        # Test with a specific filename
        url = reverse("latex:get_pdf")
        filename = "blabla"
        response = self.client.post(url, {"filename": filename})
        self.assertEqual('application/pdf', response['Content-Type'])
        self.assertTrue(filename in response['Content-Disposition'])

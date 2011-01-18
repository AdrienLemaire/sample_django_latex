# from python
import datetime

# from django
from django.conf import settings
from django.test import TestCase
from django.core.urlresolvers import reverse


class LatexViewTest(TestCase):
    """Testing views"""

    def tearDown(self):
        settings.DEBUG_PDF = False

    def test_home(self):
        "Verify if we get the home page"
        url = reverse("latex:home")
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        # Verify if the link to get a pdf is present
        self.assertContains(response, reverse("latex:get_pdf"))

    def test_get_pdf(self):
        "Verify that we get a pdf"
        # Basic test
        url = reverse("latex:get_pdf")
        response = self.client.post(url)
        self.assertEqual('application/pdf', response['Content-Type'])
        # Default filename = "test.pdf"
        self.assertTrue("test.pdf" in response['Content-Disposition'])

        # Test with a specific filename
        url = reverse("latex:get_pdf")
        filename = "blabla"
        response = self.client.post(url, {"filename": filename})
        self.assertEqual('application/pdf', response['Content-Type'])
        self.assertTrue("%s.pdf" % filename in response['Content-Disposition'])

    def test_pdf_content(self):
        settings.DEBUG_PDF = True
        url = reverse("latex:get_pdf")
        response = self.client.post(url)
        # With DEBUG_PDF = True, the response should be html instead of pdf
        self.assertEqual('text/html; charset=utf-8', response['Content-Type'])
        # Verify if the pdf contains the date of today
        #date_today = datetime.date.today().strftime("%B %d, %Y")
        #self.assertContains(response, date_today)
        # Does the file contains what we want ?
        self.assertContains(response, "File test")





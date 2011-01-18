# from django
from django.shortcuts import render_to_response
from django.template import RequestContext

# from app
from utils import generate_pdf


def home(request):
    return render_to_response("latex/home.html", {},
          context_instance=RequestContext(request))


def get_pdf(request):
    filename = request.POST.get('filename', "test")
    template = 'latex/tex/base.tex'
    template_vars = {'filename': filename}

    return generate_pdf(template, template_vars, filename)

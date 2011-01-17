# from python
import os
from subprocess import call
from tempfile import mkdtemp, mkstemp

# from django
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import render_to_string


def generate_pdf(template, template_vars, filename, dest_folder=None):
    """fill a latex template with django variables, then call pdflatex to
    create a pdf, and return the pdf"""

    tmp_folder = mkdtemp()
    os.chdir(tmp_folder)
    texfile, texfilename = mkstemp(dir=tmp_folder)
    # fill the template with vars
    os.write(texfile, render_to_string(template, template_vars))
    os.close(texfile)

    # Compile the TeX file with PDFLaTeX
    call(['pdflatex', texfilename])

    # Move resulting PDF to a more permanent location
    if not dest_folder:
        dest_folder = settings.TEX_URL
    output_filename = os.path.join(dest_folder, '%s.pdf' % filename)
    os.rename('%s.pdf' % texfilename, output_filename)

    #Remove intermediate files
    for tmp_file in os.listdir(tmp_folder):
        os.remove(tmp_file)
    os.rmdir(tmp_folder)

    # Return pdf
    result = file(output_filename, 'rb').read()
    response = HttpResponse(result, mimetype='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="%s.pdf"' % filename
    return response

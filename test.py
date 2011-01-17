import os
from subprocess import call
from tempfile import mkdtemp, mkstemp
from django.template.loader import render_to_string
# In a temporary folder, make a temporary file
dest_folder = "/home/Fandekasp/Documents/Programming/LaTeX/django-test/"
tmp_folder = mkdtemp()
os.chdir(tmp_folder)
texfile, texfilename = mkstemp(dir=tmp_folder)
# Pass the TeX template through Django templating engine and into the temp file
os.write(texfile, render_to_string('tex/base.tex', {'var': 'whatever'}))
os.close(texfile)
# Compile the TeX file with PDFLaTeX
call(['pdflatex', texfilename])
# Move resulting PDF to a more permanent location
os.rename(texfilename + '.pdf', dest_folder)
# Remove intermediate files
os.remove(texfilename)
os.remove(texfilename + '.aux')
os.remove(texfilename + '.log')
os.rmdir(tmp_folder)
print os.path.join(dest_folder, texfilename + '.pdf')

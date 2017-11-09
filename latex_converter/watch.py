import os

texdir = "~/"


for filename in filelist:
    os.system("pdflatex '" +filename+"'")
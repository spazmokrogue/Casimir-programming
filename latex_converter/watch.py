try:
    while True:
        if changed:
            os.system('pdflatex ../tex/main.tex')
except KeyboardInterrupt:
 print("Shutting down nicely...")

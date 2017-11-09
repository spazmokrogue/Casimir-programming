#print('Hello world!')

import os, time
path_to_watch = "../tex/"
before = dict ([(f, None) for f in os.listdir (path_to_watch)])
try:
  while True:
    print("Watching for changed files...")
    time.sleep (10)
    after = dict ([(f, None) for f in os.listdir (path_to_watch)])
    added = [f for f in after if not f in before]
    removed = [f for f in before if not f in after]
    if added: 
      print("Added: ", ", ".join (added))
      changed = True
    if removed: 
      print("Removed: ", ", ".join (removed))
      changed = True
    if changed:
      os.system("pdflatex "+path_to_watch+"main.tex")
    before = after
    changed = False
except KeyboardInterrupt:
  print("Shutting down nicely...")

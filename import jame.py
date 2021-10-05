import jame
def run(runfile,salam2):
  jame.salam =  salam2
  with open(runfile,"r") as rnf:
    exec(rnf.read())
salam2 = 10
run('jame.py',salam2)
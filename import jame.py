from jame import arman
with open("jame.py","r") as jame:
  exec(jame.read())
'''
def run(runfile):
  with open(runfile,"r") as rnf:
    exec(rnf.read(20))
run('jame.py')
'''
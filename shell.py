import os
import shutil
from zipfile import ZipFile
from os import path
from shutil import make_archive

p = path.realpath("test.txt")
a,b=path.split(p)
print a
print b

copyname = p + ".bak"
shutil.copy(p, copyname) 


#shutil.make_archive("zipfile", "zip", a)
with ZipFile("testzip.zip","w") as zz:
      zz.write("test.txt") 
      zz.write("test.txt.bak")
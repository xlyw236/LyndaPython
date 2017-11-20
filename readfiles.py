def readfile():
 b = open("test.txt", "r")
 c=b.readlines()
 for i in c:
  print i

readfile()
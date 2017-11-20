class class1():
 def method1(self):
  print "a"
 def method2(self):
  print "b"
  
class myclass(class1):
 def method3(self):
  print "c"
 def method4(self):
  class1.method1(self)
a=class1()
a.method2()  
c=myclass()
c.method4()
import os
from os import path
import datetime
from datetime import date, time, timedelta
import time

print path.exists("test.txt")
print path.isfile("test.txt")
print path.isdir("test.txt")
print time.ctime(path.getmtime("test.txt"))
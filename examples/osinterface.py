import os

print os.getcwd()

print dir(os)

import shutil
# shutil.copyfile('data.db', 'archive.db')
# shutil.move('/build/executables', 'installdir')

import math

print math.cos(math.pi / 4.0)
print math.log(1024, 2)

"""import smtplib
server = smtplib.SMTP('localhost')
server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
To: jcaesar@example.org
From: soothsayer@example.org
Beware the Ides of March.
")
server.quit()"""

from datetime import date
print date.today()

import zlib

s = 'witch which has which witches wrist watch'
print zlib.compress(s)

from timeit import Timer

print Timer('t=a; a=b; b=t', 'a=1; b=2').timeit(), "sec"

from string import Template
t = Template('${village}folk send $$10 to $cause.')
print t.substitute(village='Nottingham', cause='the ditch fund')
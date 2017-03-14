#!/usr/bin/env python3

import glob
import os
import datetime

times = []

for filename in glob.iglob('/home/zlsa/projects/online/infographics/data/images/**/*.svg', recursive=True):

  dt = datetime.datetime.utcfromtimestamp(os.path.getmtime(filename))
  iso_format = dt.isoformat() + 'Z'

  new_filename = filename.replace('/home/zlsa/projects/online/infographics/data/images/', '');
  times.append((new_filename, iso_format))

  continue

  new_filename = filename.replace('/home/zlsa/projects/online/infographics/data/images/', '../infographic/');
  
  os.system('mkdir -p ' + os.path.dirname(new_filename))
  os.system('cp ' + filename + ' ' + new_filename)

  filename = new_filename[len('../infographic/'):]

  os.system('./process-infographic.sh ' + filename)

times.sort()

for i in times:
  x, y = i[0].split('/')
  
  filename = '../content/infographic/' + i[0].replace('.svg', '.md')

  if os.path.exists(filename): continue

  print("{:<20}{:<80}{}".format(x, y, i[1]))

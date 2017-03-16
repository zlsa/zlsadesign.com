#!/usr/bin/env python3

import glob
import os

for filename in glob.iglob('../infographic/**/*.svg', recursive=True):
  filename = filename[len('../infographic/'):]

  if 'elements' in filename:
    continue

  os.system('./process-infographic.sh ' + filename)

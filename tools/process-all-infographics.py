#!/usr/bin/env python3

import glob
import os

for filename in glob.iglob('../infographic/**/*.svg', recursive=True):
  filename = filename[len('../infographic/'):]

  os.system('./process-infographic.sh ' + filename)

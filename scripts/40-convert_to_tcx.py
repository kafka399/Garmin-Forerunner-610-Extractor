#!/usr/bin/python
#
# Script to run the FIT-to-TCX converter on every new FIT file that is being
# downloaded by Garmin-Extractor.
#
# Adjust the fittotcx path to point to where you have put the FIT-to-TCX files.
#
# Copyright (c) 2012, Gustav Tiger <gustav@tiger.name>
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

import sys
import os
import subprocess

fittotcx = "/path/to/FIT-to-TCX/fittotcx.py"

action   = sys.argv[1]
filename = sys.argv[2]

basedir  = os.path.split(os.path.dirname(filename))[0]
basefile = os.path.basename(filename)

# Create directory
targetdir = os.path.join(basedir, "tcx")
try:
    os.mkdir(targetdir)
except:
    pass

targetfile = os.path.splitext(basefile)[0] + ".tcx"

# Run FIT-to-TCX
process = subprocess.Popen([fittotcx, filename], stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE)
(data, _) = process.communicate()

# Write result
if process.returncode == 0:
    f = file(os.path.join(targetdir, targetfile), 'w')
    f.write(data)
    f.close()


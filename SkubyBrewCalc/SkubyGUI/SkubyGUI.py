#!/usr/bin/python

################################################################################
#
# Refer to "LICENSE" for licensing information
#
# Author: John Skubic
# Email:  skubicjj@gmail.com
# Date:   12/16/17 
#
# Description: 
#
################################################################################

import sys
from PyQt4.QtGui import *

def launchSkubyGUI (argv):
  a = QApplication(argv)
  w = QWidget()
  w.resize(320,240)
  w.setWindowTitle('SkubyBrewCalc')
  w.show()
  sys.exit(a.exec_())


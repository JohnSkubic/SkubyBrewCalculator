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

from Ingredient import Ingredient
from LegalOptions import legal_hop_types

class Hop (Ingredient):

  ##### BEGIN VARIABLES #####

  # Private Vars
  _legal_uses  = ["Dry Hop",
                  "Boil",
                  "Mash",
                  "First Wort",
                  "Aroma",
                  "Whirlpool",  
                  "Hopback"]


  _aa = 0
  _boil_time = 0
  _type = ""
  _use = ""
  _ibus = 0
  _aaus = 0


  # Public Vars

  ##### BEGIN FUNCTIONS #####

  # Private Functions

  def __init__ (self, amount, unit):
    Ingredient.__init__(self, amount, unit)
    print "Added Hop" 
 
  # Public Functions

  # Get and Set Methods


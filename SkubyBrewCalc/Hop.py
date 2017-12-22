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
from LegalOptions import legal_hops,HOP_AA_IDX,HOP_ID_IDX

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
  _id = 0
  _boil_time = 0
  _type = ""
  _use = ""
  _ibus = 0
  _aaus = 0


  # Public Vars

  ##### BEGIN FUNCTIONS #####

  # Private Functions

  def __init__ (self, amount, unit, name):
    self._options = legal_hops
    self._legal_options = self._options.keys()
    Ingredient.__init__(self, amount, unit, name)
    self._aa = self._options[name][HOP_AA_IDX]
    self._id = self._options[name][HOP_ID_IDX]
 
  # Public Functions

  def print_ingredient (self):
    Ingredient.print_ingredient(self)
    print "AA: %d" % (self._aa)

  # Get and Set Methods


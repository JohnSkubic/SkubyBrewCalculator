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
from LegalOptions import legal_fermentables,FERMENTABLES_TYPE_IDX, FERMENTABLES_SUBTYPE_IDX
from LegalOptions import FERMENTABLES_COLOR_IDX, FERMENTABLES_PPG_IDX, FERMENTABLES_ID_IDX
from Util import *

class Fermentable (Ingredient):

  ##### BEGIN VARIABLES #####

  # Private Vars

  _type = ""
  _subtype = ""
  _color = 0
  _ppg = 0
  _id = 0

  # Public Vars

  ##### BEGIN FUNCTIONS #####

  # Private Functions

  def __init__ (self, amount, unit, name):
    self._options = legal_fermentables
    self._legal_options = self._options.keys()
    Ingredient.__init__(self, amount, unit, name)
    ingr_list = self._options[name]
    self._type    = ingr_list[FERMENTABLES_TYPE_IDX]
    self._subtype = ingr_list[FERMENTABLES_SUBTYPE_IDX]
    self._color   = ingr_list[FERMENTABLES_COLOR_IDX]
    self._ppg     = ingr_list[FERMENTABLES_PPG_IDX]
    self._id      = ingr_list[FERMENTABLES_ID_IDX]
 
  # Public Functions
  
  def print_ingredient (self):
    Ingredient.print_ingredient(self)
    print "Type: %s" % (self._type)
    print "Subtype: %s" % (self._subtype)
    print "color: %d" % (self._color)
    print "ppg: %d" % (self._ppg)

  # Get and Set Methods

  def get_gravity (self, efficiency, batch_size):
    amount = convert_amounts(self._amount, self._unit, "lb")
    if self._type == "Grain": # use efficiency
      return amount * self._ppg * efficiency / batch_size
    else:
      return amount *  self._ppg / batch_size


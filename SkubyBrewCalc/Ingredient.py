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

from BrewException import BrewException
from Util import *

class Ingredient ():

  ##### BEGIN VARIABLES #####

  # Private Vars
  # TODO: Legal units should come from legal options
  _legal_units = ["oz", "lb", "g", "kg"]
  _amount = 0
  _unit = 0
  _name = ""
  _legal_options = []
  _options = {}

  # Public Vars

  ##### BEGIN FUNCTIONS #####

  # Private Functions

  def __init__ (self, amount, unit, name):
    self._amount = amount
    self._unit = unit
    self._name = name
    if not name in self._legal_options:
      raise BrewException(BrewException.E_INVALID_INGREDIENT)
    
  # Public Functions

  # Get and Set Methods
  
  def print_ingredient (self):
    print "Name: %s" % (self._name)
    print "Amount: %d %s" % (self._amount, self._unit)

  def set_amount(self, amount):
    self._amount = amount

  def set_unit(self, unit):
    if not unit in self._legal_units:
      pass #exception

    self._amount = convert_amounts(self._amount, self._unit, unit)

  def get_amount(self):
    return _amount

  def set_unit(self, unit):
    pass


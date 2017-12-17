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

class Ingredient ():

  ##### BEGIN VARIABLES #####

  # Private Vars
  # TODO: Legal units should come from legal options
  _legal_units = ["oz", "lb", "g", "kg"]
  _amount = 0
  _unit = 0
  _legal_options = []
  _options = {}

  # Public Vars

  ##### BEGIN FUNCTIONS #####

  # Private Functions

  def __init__ (self, amount, unit, name):
    self._amount = amount
    self._unit = unit
    if not name in self._legal_options:
      raise BrewException(BrewException.E_INVALID_INGREDIENT)
    
  # Public Functions

  # Get and Set Methods

  def set_amount(self, amount):
    pass

  def get_amount(self):
    return _amount

  def set_unit(self, unit):
    pass


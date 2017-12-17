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

class Ingredient ():

  ##### BEGIN VARIABLES #####

  # Private Vars
  _legal_units = ["oz", "lb", "g", "kg"]
  _amount = 0
  _unit = 0

  # Public Vars

  ##### BEGIN FUNCTIONS #####

  # Private Functions

  def __init__ (self, amount, unit):
    self._amount = amount
    self._unit = unit
    
  # Public Functions

  # Get and Set Methods

  def set_amount(self, amount):
    pass

  def get_amount(self):
    return _amount

  def set_unit(self, unit):
    pass


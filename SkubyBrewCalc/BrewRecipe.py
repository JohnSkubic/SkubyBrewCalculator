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
from Hop import Hop

class BrewRecipe ():

  ##### BEGIN VARIABLES #####

  # Private Vars

  # Public Vars
  _grains = []
  _fermentables = []
  _hops = [] 

  ##### BEGIN FUNCTIONS #####

  # Private Functions
 
  def __init__ (self):
    self._grains = []
    self._fermentables = []
    self._hops = []
 
  # Public Functions
   
  def add_hop(self, amount, unit):
    self._hops.append(Hop(amount, unit)) 

  def print_recipe(self):
    pass 

  def test (self):
    print "tests"

  # Get and Set Methods



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
from Fermentable import Fermentable
from Yeast import Yeast

class BrewRecipe ():

  ##### BEGIN VARIABLES #####

  # Private Vars

  # Public Vars
  _grains = []
  _fermentables = []
  _hops = []
  _yeast = None 

  ##### BEGIN FUNCTIONS #####

  # Private Functions
 
  def __init__ (self):
    self._fermentables = []
    self._hops = []
 
  # Public Functions
   
  def add_hop(self, amount, unit, name):
    self._hops.append(Hop(amount, unit, name)) 

  def add_fermentable(self, amount, unit, name):
    self._fermentables.append(Fermentable(amount, unit, name))

  def set_yeast(self, name):
    self._yeast = Yeast(0,0, name)

  def print_recipe(self):
    print "Hops:\n"
    for hop in self._hops: 
      hop.print_ingredient()
      print ""
    print "Fermentables:\n"
    for fermentable in self._fermentables:
      fermentable.print_ingredient()
      print ""
    print "Yeast:\n"
    if self._yeast != None:
      self._yeast.print_ingredient()

  # Get and Set Methods



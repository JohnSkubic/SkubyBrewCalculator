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
from Util import *

class BrewRecipe ():

  ##### BEGIN VARIABLES #####

  # Private Vars

  # Public Vars

  # ingredients
  _grains = []
  _fermentables = []
  _hops = []
  _yeast = None 

  # others

  _boil_time = 60
  _batch_volume = 5
  _boil_unit = "gal"

  _original_gravity = 0.0 
  _final_gravity = 0.0
  _efficiency = 0.7

  ##### BEGIN FUNCTIONS #####

  # Private Functions
 
  def __init__ (self):
    self._fermentables = []
    self._hops = []
    self._boil_time = 60
 
  # Public Functions
   
  def add_hop(self, amount, unit, name, use, *args):
    self._hops.append(Hop(amount, unit, name, use, args)) 

  def add_fermentable(self, amount, unit, name):
    self._fermentables.append(Fermentable(amount, unit, name))

  def set_yeast(self, name):
    self._yeast = Yeast(0,0, name)

  def set_efficiency(self, eff):
    self._efficiency = eff

  def get_efficiency(self):
    return self._efficiency

  def get_ibus(self):
    batch_vol = convert_volume(self._batch_volume, self._boil_unit, "L")
    ibus = 0.0
    for hop in self._hops:
      ibus = ibus + hop.get_ibus(self._original_gravity, batch_vol, self._boil_time)
    return ibus

  def get_og(self):
    batch_vol = convert_volume(self._batch_volume, self._boil_unit, "gal")
    gravity = 0.0
    for fermentable in self._fermentables:
      gravity = gravity + fermentable.get_gravity(self._efficiency, batch_vol)
    gravity = gravity / 1000.0 + 1
    self._original_gravity = gravity
    return gravity

  def get_fg(self):
    if self._yeast != None:
      fg = self._original_gravity - 1.0
      fg = fg * (1-self._yeast.get_attenuation())
      self._final_gravity = fg + 1.0
    else:
      self._final_gravity = 1.0
    return self._final_gravity

  def get_abv(self):
    return (self._original_gravity-self._final_gravity)*1.05/self._final_gravity/0.79
  
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



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
import yaml 
import copy 

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
   
  def add_hop(self, amount, unit, name, use, form, boil_time=None):
    my_hop = Hop()
    my_hop.init_full_by_name(name, amount, unit, use, form, boil_time)
    self._hops.append(my_hop) 

  def add_fermentable(self, amount, unit, name):
    my_fermentable = Fermentable()
    my_fermentable.init_full_by_name(name, amount, unit)
    self._fermentables.append(my_fermentable)

  def set_yeast(self, name):
    self._yeast = Yeast()
    self._yeast.init_by_name(name)
    
  def set_efficiency(self, eff):
    self._efficiency = eff

  def get_efficiency(self):
    return self._efficiency

  def get_ibus(self):
    batch_vol = convert_volume(self._batch_volume, self._boil_unit, "gal")
    ibus = 0.0
    for hop in self._hops:
      ibus = ibus + hop.get_ibus(self._original_gravity, batch_vol, self._boil_time)
    return ibus

  def get_srm(self):
    srm = 0.0
    batch_vol = convert_volume(self._batch_volume, self._boil_unit, "gal")
    for fermentable in self._fermentables:
      srm = srm + fermentable.get_srm(batch_vol)
    return srm

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
 
  def get_stats(self):
    og  = self.get_og()
    fg  = self.get_fg()
    abv = self.get_abv()
    ibu = self.get_ibus()
    srm = self.get_srm()
    return og,fg,abv,ibu,srm

  def save_recipe(self, filename):
    #convert recipe to 5 gallon units
    ratio = 5.0 / convert_volume(self._batch_volume, self._boil_unit, "gal")
    hop_copy = copy.deepcopy(self._hops)
    fermentables_copy = copy.deepcopy(self._fermentables)
    for hop in hop_copy:
      hop.set_amount(hop.get_amount()*ratio)
      hop.set_unit("oz")
    for fermentable in fermentables_copy:
      fermentable.set_amount(fermentable.get_amount()*ratio)
      fermentable.set_unit("lb")
    
    #store recipe
    store_dict = {}
    ingr_list = []

    for hop in hop_copy:
      ingr_list.append(hop.to_dict())
    for fermentable in fermentables_copy:
      ingr_list.append(fermentable.to_dict())
    ingr_list.append(self._yeast.to_dict())

    store_dict["INGREDIENTS"] = ingr_list
    with open(filename, "w") as f:
      yaml.dump(store_dict, f)

  def load_recipe(self, filename):
    self._hops = []
    self._fermentables = []
    self._yeast = None

    with open(filename, "r") as f:
      loaded = yaml.safe_load(f)

    ingr_list = loaded["INGREDIENTS"]
    for ingr in ingr_list:
      if ingr["ingredient"] == "hop":
        my_hop = Hop()
        my_hop.init_from_dict(ingr)
        self._hops.append(my_hop)
      elif ingr["ingredient"] == "fermentable":
        my_fermentable = Fermentable()
        my_fermentable.init_from_dict(ingr)
        self._fermentables.append(my_fermentable)
      elif ingr["ingredient"] == "yeast":
        my_yeast = Yeast()
        my_yeast.init_from_dict(ingr)
        self._yeast = my_yeast
      
 
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



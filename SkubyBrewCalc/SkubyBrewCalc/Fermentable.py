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
from LegalOptionsUtil import *
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

  def __init__ (self):
    self._options = legal_fermentables
    self._legal_options = self._options.keys()
    Ingredient.__init__(self)


  def to_dict (self):
    out_dict = {}
    out_dict["ingredient"] = "fermentable"
    out_dict["id"] = self._id
    out_dict["name"] = self._name
    out_dict["amount"] = self._amount
    out_dict["unit"] = self._unit
    return out_dict 

  def init_from_dict (self, in_dict):
    self._id = in_dict["id"]
    self._name = in_dict["name"]
    self._amount = in_dict["amount"]
    self._unit = in_dict["unit"]
    self.init_by_id(self._id)
 
  # Public Functions

  def init_by_name(self, name):
    Ingredient.init_by_name(self,name)
    ingr_list = self._options[name]
    self._type    = ingr_list[FERMENTABLES_TYPE_IDX]
    self._subtype = ingr_list[FERMENTABLES_SUBTYPE_IDX]
    self._color   = ingr_list[FERMENTABLES_COLOR_IDX]
    self._ppg     = ingr_list[FERMENTABLES_PPG_IDX]
    self._id      = ingr_list[FERMENTABLES_ID_IDX]
    self._name    = name

  def init_full_by_name(self, name, amount, unit):
    self.init_by_name(name)
    self.set_all(amount, unit)

  def init_by_id(self, my_id):
    name = get_fermentable_by_id(my_id)
    self.init_by_name(name)
    
  def set_all(self, amount, unit):
    Ingredient.set_all(self, amount, unit) 
 
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

  def get_srm (self, batch_size):
    # Morey equation
    amount_lbs = convert_amounts(self._amount, self._unit, "lb")
    mcu = self._color*amount_lbs/batch_size
    srm = 1.4922* pow(mcu,0.6859)
    return srm 

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
from BrewException import BrewException
from LegalOptions import legal_hops,HOP_AA_IDX,HOP_ID_IDX
from LegalOptions import legal_hop_uses, legal_hop_forms
from Util import *
from math import exp 

class Hop (Ingredient):

  ##### BEGIN VARIABLES #####

  # Private Vars
  _legal_uses  = []
  _legal_forms = []

  _aa = 0
  _id = 0
  _boil_time = 0
  _type = ""
  _use = ""
  _form = ""

  # Public Vars

  ##### BEGIN FUNCTIONS #####

  # Private Functions

  def __init__ (self, amount, unit, name, use, *args):
    self._options = legal_hops
    self._legal_uses = legal_hop_uses
    self._legal_options = self._options.keys()
    self._legal_forms = legal_hop_forms
    Ingredient.__init__(self, amount, unit, name)
    self._aa = self._options[name][HOP_AA_IDX]
    self._id = self._options[name][HOP_ID_IDX]
    self.set_use(use, args)    
    self._form = "pellet"

  # Public Functions

  def print_ingredient (self):
    Ingredient.print_ingredient(self)
    print "AA: %d" % (self._aa)
    print "Use: %s" % (self._use)
    print "Form: %s" % (self._form)
    if self._use == "Boil":
      print "Boil Time: %d" % (self._boil_time)

  def _get_utilization(self,time):
    # U = 1 - e^(-0.04t) 
    print "TIME: %s " % (time) 
    return util  

  # Get and Set Methods
  
  def set_amount (self, amount):
    Ingredient.set_amount(amount) 

  def set_use (self, use, *args):
    if not use in self._legal_uses:
      raise BrewException(BrewException.E_INVALID_HOP_USE) 
    self._use = use
    if use == "Boil":
      self._boil_time = args[0][0][0]

  def get_ibus (self, gravity, volume, boil_time):
    aaus = self.get_aaus()
    if self._use == "Mash":
      boil_fact = (1.0 - exp(-0.04 * float(boil_time))) / 4.15
    else:
      boil_fact = (1.0 - exp(-0.04 * float(self._boil_time))) / 4.15
    bigness_fact = 1.65 * pow(0.000125, gravity-1)
    util = boil_fact * bigness_fact
    if self._form == "pellet":
      util = util * 1.1
    return  aaus*util*74.9/volume 

  def get_aaus (self):
    w_oz = convert_amounts(self._amount, self._unit, "oz")
    return w_oz*self._aa

  def set_form (self, new_form):
    if not new_form in self._legal_forms:
      raise BrewException(BrewException.E_INVALID_HOP_FORM)
    self._form = new_form 

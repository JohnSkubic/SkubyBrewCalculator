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
from LegalOptions import legal_hop_uses

class Hop (Ingredient):

  ##### BEGIN VARIABLES #####

  # Private Vars
  _legal_uses  = []

  _aa = 0
  _id = 0
  _boil_time = 0
  _type = ""
  _use = ""

  _ibus = 0
  _aaus = 0


  # Public Vars

  ##### BEGIN FUNCTIONS #####

  # Private Functions

  def __init__ (self, amount, unit, name, use, *args):
    self._options = legal_hops
    self._legal_uses = legal_hop_uses
    self._legal_options = self._options.keys()
    Ingredient.__init__(self, amount, unit, name)
    self._aa = self._options[name][HOP_AA_IDX]
    self._id = self._options[name][HOP_ID_IDX]
    self.set_use(use, args)    

  def _calc_bitterness(self):
    print "TODO: Implement calc bitterness"
    self._ibus = 0
    self._aaus = 0

  # Public Functions

  def print_ingredient (self):
    Ingredient.print_ingredient(self)
    print "AA: %d" % (self._aa)
    print "Use: %s" % (self._use)
    if self._use == "Boil":
      print "Boil Time: %d" % (self._boil_time)

  # Get and Set Methods
  
  def set_amount (self, amount):
    Ingredient.set_amount(amount) 
    self._calc_bitterness()

  def set_use (self, use, *args):
    if not use in self._legal_uses:
      raise BrewException(BrewException.E_INVALID_HOP_USE) 
    self._use = use
    if use == "Boil":
      self._boil_time = args[0][0]
    self._calc_bitterness()

  def get_ibus (self):
    return self._ibus

  def get_aaus (self):
    return self._aaus

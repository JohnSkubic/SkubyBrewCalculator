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

  # chart for utilization calculation
  # indices are for the following gravities:
  # 1.030 1.040 1.050 ... 1.120
  # Each index matches with a boil time starting at 0 and moving up by 5 min to 120 min
  _util = [ [0,     0,      0,      0,      0,      0,      0,      0,      0,      0],
            [0.055, 0.05,   0.046,  0.042,  0.038,  0.035,  0.032,  0.029,  0.027,  0.025], 
            [0.1,   0.091,  0.084,  0.076,  0.07,   0.064,  0.058,  0.053,  0.049,  0.045], 
            [0.137, 0.125,  0.114,  0.105,  0.096,  0.087,  0.080,  0.073,  0.067,  0.061],
            [0.167, 0.153,  0.140,  0.128,  0.117,  0.107,  0.098,  0.089,  0.081,  0.074],
            [0.192, 0.175,  0.160,  0.147,  0.134,  0.122,  0.112,  0.102,  0.094,  0.085],
            [0.212, 0.194,  0.177,  0.162,  0.148,  0.135,  0.124,  0.113,  0.103,  0.094],
            [0.229, 0.209,  0.191,  0.175,  0.160,  0.146,  0.133,  0.122,  0.111,  0.102],
            [0.242, 0.221,  0.202,  0.185,  0.169,  0.155,  0.141,  0.129,  0.118,  0.10],
            [0.253, 0.232,  0.212,  0.194,  0.177,  0.162,  0.148,  0.135,  0.123,  0.113],
            [0.263, 0.240,  0.219,  0.200,  0.183,  0.168,  0.153,  0.140,  0.128,  0.117],
            [0.270, 0.247,  0.226,  0.206,  0.188,  0.172,  0.157,  0.144,  0.132,  0.120],
            [0.276, 0.252,  0.231,  0.211,  0.193,  0.176,  0.161,  0.147,  0.135,  0.123],
            [0.285, 0.261,  0.238,  0.218,  0.199,  0.182,  0.166,  0.152,  0.139,  0.127],
            [0.291, 0.266,  0.243,  0.222,  0.203,  0.186,  0.170,  0.155,  0.142,  0.130],
            [0.295, 0.270,  0.247,  0.226,  0.206,  0.188,  0.172,  0.157,  0.144,  0.132],
            [0.298, 0.272,  0.249,  0.228,  0.208,  0.190,  0.174,  0.159,  0.145,  0.133],
            [0.300, 0.274,  0.251,  0.229,  0.209,  0.191,  0.175,  0.160,  0.146,  0.134],
            [0.301, 0.275,  0.252,  0.230,  0.210,  0.192,  0.176,  0.161,  0.147,  0.134]]


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

  # Public Functions

  def print_ingredient (self):
    Ingredient.print_ingredient(self)
    print "AA: %d" % (self._aa)
    print "Use: %s" % (self._use)
    if self._use == "Boil":
      print "Boil Time: %d" % (self._boil_time)

  def _get_utilization(self, grav, time):
    grav_idx = int(grav*100) - 103
    time_idx = time/5
    
    if time_idx > 19:
      raise BrewException(BrewException.E_INVALID_IBU_TIME) 
    if grav_idx < 0 or grav_idx > 10:
      raise BrewException(BrewException.E_INVALID_IBU_GRAVITY)

    return _util[time_idx][grav_idx]

  # Get and Set Methods
  
  def set_amount (self, amount):
    Ingredient.set_amount(amount) 

  def set_use (self, use, *args):
    if not use in self._legal_uses:
      raise BrewException(BrewException.E_INVALID_HOP_USE) 
    self._use = use
    if use == "Boil":
      self._boil_time = args[0][0]

  def get_ibus (self, gravity, volume, boil_time):
    aaus = self.get_aaus()
    if self._use == "Mash":
      util = _get_utilization(gravity, boil_time)
    else:
      util = _get_utilization(gravity, self._boil_time)
    return aaus*util*75/volume

  def get_aaus (self):
    w_oz = convert_amounts(self._amount, self._unit, "oz")
    return w_oz*self._aa

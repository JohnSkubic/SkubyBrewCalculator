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
from LegalOptions import legal_yeasts, YEAST_LAB_IDX, YEAST_CODE_IDX, YEAST_TYPE_IDX
from LegalOptions import YEAST_FLOCCULATION_IDX, YEAST_ATTENUATION_IDX
from LegalOptions import YEAST_MIN_TEMP_IDX, YEAST_MAX_TEMP_IDX, YEAST_ID_IDX
from LegalOptionsUtil import *

class Yeast (Ingredient):

  ##### BEGIN VARIABLES #####

  # Private Vars

  _lab = ""
  _code = ""
  _type = ""
  _flocculation = "" 
  _attenuation = 0
  _min_tmep = 0
  _max_temp = 0
  _id = 0

  # Public Vars

  ##### BEGIN FUNCTIONS #####

  # Private Functions

  def __init__ (self):
    self._options = legal_yeasts
    self._legal_options = self._options.keys()
    Ingredient.__init__(self)


  def init_by_name(self, name):
    Ingredient.init_by_name(self,name)
    ingr_list = self._options[name]
    self._lab           = ingr_list[YEAST_LAB_IDX]
    self._code          = ingr_list[YEAST_CODE_IDX]
    self._type          = ingr_list[YEAST_TYPE_IDX]
    self._flocculation  = ingr_list[YEAST_FLOCCULATION_IDX]
    self._attenuation   = ingr_list[YEAST_ATTENUATION_IDX]
    self._min_temp      = ingr_list[YEAST_MIN_TEMP_IDX]
    self._max_temp      = ingr_list[YEAST_MAX_TEMP_IDX]
    self._id            = ingr_list[YEAST_ID_IDX]
    self.amount = 0

  def init_by_id(self, my_id):
    name = get_yeast_by_id(my_id)
    self.init_by_name(name)

 
  # Public Functions

  def print_ingredient (self):
    Ingredient.print_ingredient(self)
    print "Lab: %s"           % (self._lab)
    print "Code: %s"          % (self._code)
    print "Type: %s"          % (self._type)
    print "Flocculation: %s"  % (self._flocculation)
    print "Attenuation: %d "  % (self._attenuation)
    print "Min Temp: %d"      % (self._min_temp)
    print "Max Temp: %d"      % (self._max_temp)

  # Get and Set Methods

  def get_attenuation (self):
    return (self._attenuation / 100.0)

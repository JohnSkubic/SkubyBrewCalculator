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

class BrewException (Exception):

  ##### BEGIN VARIABLES #####

  # Exceptions
  E_INVALID_INGREDIENT = "INVALID_INGREDIENT"

  ##### BEGIN FUNCTIONS #####

  def __init__ (self, code, *args, **kwargs):
    self.code = code
    Exception.__init__(self, args, kwargs)
 

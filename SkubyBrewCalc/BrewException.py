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
  E_INVALID_INGREDIENT  = "INVALID_INGREDIENT"
  E_INVALID_HOP_USE     = "INVALID_HOP_USE"
  E_INVALID_IBU_GRAVITY = "INVALID_IBU_GRAVITY"
  E_INVALID_IBU_TIME    = "INVALID_IBU_TIME"
  E_INVALID_HOP_FORM    = "INVALID_HOP_FORM"

  ##### BEGIN FUNCTIONS #####

  def __init__ (self, code, *args, **kwargs):
    self.code = code
    Exception.__init__(self, args, kwargs)
 

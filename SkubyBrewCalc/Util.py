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

def convert_amounts(in_amount, in_unit, out_unit):
  #convert to oz
  in_oz = float(in_amount)
  if in_unit == "lb":
    in_oz = float(in_amount) * 16.0
  elif in_unit == "g":
    in_oz = float(in_amount) * 0.035274
  elif in_unit == "kg":
    in_oz = float(in_amount) * 35.274

  #convert to target 
  out_oz = in_oz
  if out_unit == "lb":
    out_oz = in_oz / 16.0
  elif out_unit == "g":
    out_oz = in_oz / 0.035274
  elif out_unit == "kg":
    out_oz = in_oz / 35.274

  return out_oz 

def convert_volume(in_amount, in_unit, out_unit):
  if in_unit == "gal":
    return float(in_amount) * 3.785
  else:
    return float(in_amount) / 3.785


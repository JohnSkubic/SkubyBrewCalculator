#!/usr/bin/python

################################################################################
#
# Refer to "LICENSE" for licensing information
#
# Author: John Skubic
# Email:  skubicjj@gmail.com
# Date:   12/16/17 
#
# Description: Contains functions for accessing the legal options 
#
################################################################################

# Hop includes
from LegalOptions import legal_hops,HOP_AA_IDX, HOP_ID_IDX

from LegalOptions import legal_fermentables,FERMENTABLES_TYPE_IDX, FERMENTABLES_SUBTYPE_IDX
from LegalOptions import FERMENTABLES_COLOR_IDX, FERMENTABLES_PPG_IDX, FERMENTABLES_ID_IDX

from LegalOptions import legal_yeasts, YEAST_LAB_IDX, YEAST_CODE_IDX, YEAST_TYPE_IDX
from LegalOptions import YEAST_FLOCCULATION_IDX, YEAST_ATTENUATION_IDX
from LegalOptions import YEAST_MIN_TEMP_IDX, YEAST_MAX_TEMP_IDX, YEAST_ID_IDX

# Common functions

def _get_name_by_id (ingr_id, option_dict, id_idx):
  for key in option_dict.keys():
    if option_dict[key][id_idx] == ingr_id:
      return key
  return None

def _get_unique_options (option_dict, idx):
  unique_options = []
  for key in option_dict.keys():
    if not option_dict[key][idx] in unique_options:
      unique_options.append(option_dict[key][idx])
  return unique_options

def _get_unique_options_with_filter (option_dict, idx, filter_val, filter_idx):
  unique_options = []
  for key in option_dict.keys():
    if option_dict[key][filter_idx] == filter_val and not option_dict[key][idx] in unique_options:
      unique_options.append(option_dict[key][idx])
  return unique_options


# Hop Access Functions

def get_hop_by_id (hop_id):
  return _get_name_by_id(hop_id, legal_hops, HOP_ID_IDX)

def get_hop_list ():
  return legal_hops.keys()


# Fermentable Access Functions

def get_fermentable_by_id (fermentable_id):
  return _get_name_by_id(fermentable_id, legal_fermentables, FERMENTABLES_ID_IDX)

def get_fermentable_list ():
  return legal_fermentables.keys()

def get_fermentable_types ():
  return _get_unique_options(legal_fermentables, FERMENTABLES_TYPE_IDX)

def get_fermentable_subtypes ():
  return _get_unique_options(legal_fermentables, FERMENTABLES_SUBTYPE_IDX)

def get_fermentable_subtypes_by_type(fermentable_type):
  return _get_unique_options_with_filter(legal_fermentables, FERMENTABLES_SUBTYPE_IDX, fermentable_type, FERMENTABLES_TYPE_IDX)
  

# Yeast Access Functions

def get_yeast_by_id (yeast_id):
  return _get_name_by_id(yeast_id, legal_yeasts, YEAST_ID_IDX)

def get_yeast_list ():
  return legal_yeasts.keys()

def get_yeast_labs ():
  return _get_unique_options(legal_yeasts, YEAST_LAB_IDX)

def get_yeast_types ():
  return _get_unique_options(legal_yeasts, YEAST_TYPE_IDX)
 





 

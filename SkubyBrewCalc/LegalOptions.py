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


# START HOP OPTIONS

HOP_AA_IDX = 0

legal_hops = {
"Ahtanum"               : [5.5] ,
"Amarillo"              : [8.6] ,
"Aquila"                : [7]   ,
"B. C. Goldings"        : [5]   ,
"Banner"                : [10]  ,
"Bramling Cross"        : [6.5] ,
"Brewer's Gold"         : [9]   ,
"Bullion"               : [7.5] ,
"Cascade"               : [7]   ,
"Centennial"            : [7.8] ,
"Challenger"            : [8.5] ,
"Chinook"               : [13]  ,
"Citra"                 : [11]  ,
"Cluster"               : [6.5] ,
"Columbus"              : [15]  ,
"Comet"                 : [10]  ,
"Crystal"               : [4.3] ,
"Domesic Hallertau"     : [3.9] ,
"East Kent Goldings"    : [5]   ,
"Eroica"                : [12]  ,
"First Gold"            : [7.5] ,
"Fuggles"               : [4.5] ,
"Galena"                : [13]  ,
"Glacier"               : [5.5] ,
"Goldings"              : [4.5] ,
"Hallertau Mittelfruh"  : [3.75],
"Hallertau Hersbrucker" : [4]   ,
"Herald"                : [12]  ,
"Hersbrucker"           : [4]   ,
"Horizon"               : [12.5],
"Huller Bitterer"       : [5.75],
"Kent Goldings"         : [5]   ,
"Liberty"               : [4]   ,
"Lublin"                : [4.5] ,
"Magnum"                : [15]  ,
"Millenium"             : [15.5],
"Mount Hood"            : [4.8] ,
"Mount Rainier"         : [6.2] ,
"Motueka"               : [7.0] ,
"Nelson Sauvin"         : [12.5],
"Newport"               : [15.5],
"Northdown"             : [8.6] ,
"Northern Brewer"       : [7.8] ,
"Nugget"                : [14]  ,
"Olympic"               : [12]  ,
"Omega"                 : [10]  ,
"Orion"                 : [7]   ,
"Pacific Gem"           : [15.4],
"Perle"                 : [8.2] ,
"Phoenix"               : [10]  ,
"Pioneer"               : [9]   ,
"Pride of Ringwood"     : [10]  ,
"Progress"              : [6.25],
"Record"                : [6.5] ,
"Saaz"                  : [3.5] ,
"Santiam"               : [6.5] ,
"Satus"                 : [13]  ,
"Simcoe"                : [12.7],
"Sorachi Ace"           : [11.1],
"Spalt"                 : [4.5] ,
"Sterling"              : [8.7] ,
"Sticklebract"          : [11.5],
"Strisselspalt"         : [3.5] ,
"Styrian Goldings"      : [5.5] ,
"Super Alpha"           : [13]  ,
"Super Styrians"        : [9]   ,
"Summit"                : [18.5],
"Talisman"              : [8]   ,
"Target"                : [11.5],
"Tettnanger"            : [4.5] ,
"Tomahawk"              : [15]  ,
"Ultra"                 : [4.5] ,
"Vanguard"              : [5]   ,
"Warrior"               : [16]  ,
"Whitbread Golding"     : [6]   ,
"Willamette"            : [4.5] ,
"Wye Target"            : [10]  ,
"Yamhill Goldings"      : [4]   ,
"Yakima Cluster"        : [7]   ,
"Yeoman"                : [7.25],
"Zenith"                : [9]   ,
"Zeus"                  : [16]
}


# START 


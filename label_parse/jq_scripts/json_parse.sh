#! /bin/bash

# * * * * * * * * * * * * * * * * * * * * * #
#       _                  _                #
#    __| |  _   _    ___  | | __  ___       #
#   / _` | | | | |  / __| | |/ / / __|      #
#  | (_| | | |_| | | (__  |   <  \__ \      #
#   \__,_|  \__,_|  \___| |_|\_\ |___/      #
#                                           #
# * * * * * * * * * * * * * * * * * * * * * #


################################################################################################
## To Do 
#
# Extract data that can be public?  (no email addy's)
# remove null fields?
#
#
################################################################################################

################################################################################################
## Done
#
# Remove 6 "skip" entries - done in VScode manually
# Replace Canadian Goose with Canada Goose - done in VScode with find and replace
# Correct Spelling on Readhead to Redhead - done in VScode with find and replace
#
#
################################################################################################

## Create dataset
foo=$(cat raw_labelbox_data.json)
echo $foo | jq .
echo $foo | jq .  > prettiefied.json     # write our to 'pretty' json file

################################################
#                                              #
#          Manual Cleaning in VS Code          #
#            output > 'cleaned.json'           #
#                                              #
################################################


# How many entries? 112 (from 118)
jq '.| type,length' cleaned.json
jq '.[] | type,length' cleaned.json | sort | uniq -c

# What does an entry look like?
jq '.[0]' cleaned.json

# view and count keys in those entries
jq '.[] | keys' cleaned.json| sort | uniq -c

# get labels
jq '.[].Label | keys' cleaned.json | sort | uniq -c

:'''
"American Wigeon",
"Canada Goose",
"Gadwall",
"Mallard",
"Northern Pintail",
"Northern Shoveler",
"Other",
"Redhead",
"Ringneck",
"Ruddy",
"Sandhill Crane",
"Snow Goose",
"Teal"
'''


# Check number of Mallard Labels (geometry line count = 11775)
jq '.[].Label.Mallard' cleaned.json | sort | uniq -c

# Others // checks out with labelbox's overview page
jq '.[].Label.Other' cleaned.json | sort | uniq -c    # 1762 geometries
jq '.[].Label."Northern Pintail"' cleaned.json | sort | uniq -c    # 2369 geometries
jq '.[].Label."Northern Shoveler"' cleaned.json | sort | uniq -c # 183 geometries


# Find contributers (email / Personally Identifying Information) - needs masked
jq '.[]."Created By"' cleaned.json | sort | uniq -c

:'
"andrew_stetter@fws.gov"
"barry_wilson@fws.gov"
"bill_johnson@fws.gov"
"dan_collins@fws.gov"
"david.butler@tpwd.texas.gov"
"jeff_sanchez@fws.gov"
"jena_moon@fws.gov"
"john_vradenburg@fws.gov"
"josh_vest@fws.gov"
"jude_smith@fws.gov"
"kammie_kruse@fws.gov"
"mbrasher@ducks.org"
"ronald_deroche@fws.gov"
"stephen.mcdowell@tpwd.texas.gov"
"steven_sesnie@fws.gov"
'

















# * * * * * * * * * * * * * * * * * * * * * * * *
#     _ _ _     _   _ _    _ _ _   _ _ _ _      #
#   |       \ |  | |   | /       ||    /   |    #
#   |   |    ||  | |   ||        ||        |    #
#   |   |    ||  | |   ||  | - -  |       /     #
#   |   |    ||  | |   ||  | - - ||       \     #
#   |   |    ||  |_|   ||        ||        |    #
#   | _ _ _ / \ _ _ _ _ \\ _ _ _ || _  \ _ |    #
#                                               #
# * * * * * * * * * * * * * * * * * * * * * * * *








# * * * * * * * * * * * * * * * * * * * * * * * *
#     _ _ _     _   _ _    _ _ _   _     _      #
#   |       \ |  | |   | /       ||    /   |    #
#   |   |    ||  | |   ||    _ _ ||        |    #
#   |   |    ||  | |   ||  |      |       /     #
#   |   |    ||  | |   ||  | _ _ ||       \     #
#   |   |    ||  |_|   ||        ||        |    #
#   | _ _ _ / \ _ _ _ _ \\ _ _ _ || _  \ _ |    #
#                                               #
# * * * * * * * * * * * * * * * * * * * * * * * *







# * * * * * * * * * * * * * * * * * * * * * * * * 
#    ____    ___     ___    ____    _____       # 
#   / ___|  / _ \   / _ \  / ___|  | ____|      # 
#  | |  _  | | | | | | | | \___ \  |  _|        #  
#  | |_| | | |_| | | |_| |  ___) | | |___       # 
#   \____|  \___/   \___/  |____/  |_____|      #        
#                                               #   
# * * * * * * * * * * * * * * * * * * * * * * * *



# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 
#   References                                  
#
#    https://devblogs.nvidia.com/detectnet-deep-neural-network-object-detection-digits/    
#    https://github.com/NVIDIA/DIGITS/issues/980                                           
#    https://towardsdatascience.com/how-to-adjust-detectnet-a9ad0452d27f                   
#                                               
#
#
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 


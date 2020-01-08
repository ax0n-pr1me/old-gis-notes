

##
##
## Examining the first entry - works if not expecting high level entries to vary much
##
##

# What does an entry look like?
jq '.[0]' bnchmrk.json

# get number of entries [ = 118 ]
jq 'keys[]' bnchmrk.json
jq 'keys[]' bnchmrk.json | wc -l

# view and count keys in those entries [ = 17 ]
jq 'map(keys)[0]' bnchmrk.json -r
jq 'map(keys)[0][]' bnchmrk.json -r | wc -l

# verify the same number of keys exists across all label entries
# [ 2006 = 118 * 17 ]
jq 'map(keys)[0][]' bnchmrk.json -r  | wc -l
jq 'map(keys)[][]' bnchmrk.json -r  | wc -l

# get labels
jq 'map(.["Label"])[0]' bnchmrk.json

# get number of polygons per label
jq 'map(."Label")[0][]' bnchmrk.json | jq 'map(keys)[0]' -r | wc -l
jq 'map(."Label")[0]' bnchmrk.json | jq 'map(keys)[0]' -r







##
##
## environment variable method ($foo)
##
##

foo=$(cat bnchmrk.json)
echo $foo | jq .

#write out
#echo $foo | jq .  > ~/repo/w0rkspac3/data_refinery/bnchmrk.json

echo $foo | jq 'map(keys)' # this is the same as
echo $foo | jq '.[] | keys'
echo $foo | jq '.[] | keys' | sort | uniq -c

echo $foo | jq '. | type,length'
echo $foo | jq '.[] | type,length'
echo $foo | jq '.[] | type,length' | sort | uniq -c

# a somewhat useful aside
echo $foo | jq '.[] | .[] | type,length' | sort | uniq -c

#get list of keys and count of each
echo $foo | jq '.[] | keys' | sort | uniq -c 

# get list of agreement values
echo $foo | jq '.[].Agreement'

# see all ID entries
echo $foo | jq '.[].ID'

# Select a specifc entry by ID
echo $foo | jq '.[] | select(.ID=="ck0756lbh8z120944o2fb71ar")'

# see specifc species
echo $foo | jq '.[].Label | keys'
echo $foo | jq '.[].Label | keys' | sort | uniq -c


mkdir BNCHMRK
mv export-2020-03-12T00_03_58.773Z.json BNCHMRK/
cd BNCHMRK/
jq export-2020-03-12T00_03_58.773Z.json
jq . export-2020-03-12T00_03_58.773Z.json
jq . export-2020-03-12T00_03_58.773Z.json --pretty
jq . export-2020-03-12T00_03_58.773Z.json -pretty
jq . export-2020-03-12T00_03_58.773Z.json | less
jq .[labels]  export-2020-03-12T00_03_58.773Z.json
jq .labels  export-2020-03-12T00_03_58.773Z.json
jq .[].label  export-2020-03-12T00_03_58.773Z.json
jq .label  export-2020-03-12T00_03_58.773Z.json
jq . export-2020-03-12T00_03_58.773Z.json | less
jq .Label  export-2020-03-12T00_03_58.773Z.json
jq .[].Label  export-2020-03-12T00_03_58.773Z.json
jq .[].Label  export-2020-03-12T00_03_58.773Z.json | less
jq .[].Label."Canadian Goose"  export-2020-03-12T00_03_58.773Z.json | less
jq .[].Label  export-2020-03-12T00_03_58.773Z.json | less
jq .[]."Canadian Goose"  export-2020-03-12T00_03_58.773Z.json | less
jq .[]."Canadian Goose"  export-2020-03-12T00_03_58.773Z.json
jq .[].Label."Canadian Goose"  export-2020-03-12T00_03_58.773Z.json
jq .[].[Label].["Canadian Goose"]  export-2020-03-12T00_03_58.773Z.json
jq .[].[Label] | .["Canadian Goose"]  export-2020-03-12T00_03_58.773Z.json
jq .[].[Label]
cp export-2020-03-12T00_03_58.773Z.json db.json
clear
cat db.json | jq '.'
clear
cat db.json | jq '.Label'
cat db.json | jq '.[].Label'
cat db.json | jq '.[].Label' | less
cat db.json | jq '.[].Label.[1]'
cat db.json | jq '.[].Label.1'
cat db.json | jq '.[].Label."Canadian Goose"''
cat db.json | jq '.[].Label."Canadian Goose"'
cat db.json | jq '.[].Label."Canadian Goose"' | less
cat db.json | jq '.[].Label."Canadian Goose".geometry' | less
cat db.json | jq '.[].Label."Canadian Goose"."geometry"' | less
cat db.json | jq '.[].Label."Canadian Goose"."geometry"'
cat db.json | jq '.[].Label."Canadian Goose"'


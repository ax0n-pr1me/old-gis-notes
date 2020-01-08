a=115
for i in *.tif; do
  new=$(printf "%04d_20161210.tif" "$a") #04 pad to length of 4
  mv -i -- "$i" "$new"
  let a=a-1
done
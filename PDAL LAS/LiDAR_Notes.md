# LiDAR Porcessing Notes

## PDAL
`pdal info Cobalt_Encino_190829_150417.las`

Output into [pdal_out.txt]<pdal_out.txt>


## Method 1 - Quick PDAL Method

`pdal ground --cell_size=5 --extract input.laz out-bare-earth.laz`

## Metho 2 - In-Depth PDAL Method
[Source]<https://lists.osgeo.org/pipermail/pdal/2017-July/001367.html>
[Reference]<https://gis.stackexchange.com/questions/101786/determining-bare-earth-dem-from-unclassified-las-file>

### JSON file

```{JSON}
{
    "pipeline": [
        "inputfile.laz",
        {
            "type":"filters.smrf",
            "cell": "2.0",
            "threshold": "0.75"
        },
        {
            "type":"filters.range",
            "limits":"Classification[2:2]"
        },
        "out/smurf_classifed.las"
    ]
}
```

```{sh}
pdal pipeline "classify-ground-smrf.json"
```

## Method 2 - SPDlib
https://spectraldifferences.wordpress.com/2014/08/06/dem-spdlib/

Might not work with LAS 1.4 without rolling back to unindexed or previous (1.2) version


### Create conda env

```{sh}
conda create -n spdlib_env \
   -c conda-forge -c rios -c osgeo \
   spdlib spd3dpointsviewer tuiview
source activate spdlib_env
```

### Convert to SPD Format

```{sh}
spdtranslate --if LAS --of SPD -b 10 -x LAST_RETURN \
-i LiDAR.las -o LiDAR_10m.spd
```

### Classify Ground Returns

Progressive morphology filter [1]

```{sh}
spdpmfgrd -r 50 --overlap 10 --initelev 0.1 --maxfilter 14 -b 0.5 \
-i LiDAR_10m.spd -o LiDAR_10m_pmfgrd.spd
```
OR

SPDLib implementation of the multi-scale curvature algorithm created at the US Forest Service [2]

```{sh}
spdmccgrd -r 50 --overlap 10 -i LiDAR_10m.spd -o LiDAR_10m_mccgrd.spd
```

### Interpolate to DTM and DSM

```{sh}
# DTM
spdinterp --dtm --topo -r 50 --overlap 10 --in NATURAL_NEIGHBOR \
-f GTiff -b 1 -i LiDAR_10m_pmfgrd.spd -o LiDAR_1m_dtm.tif
 
# DSM
spdinterp --dsm --topo -r 50 --overlap 10 --in NATURAL_NEIGHBOR \
-f GTiff -b 1 -i LiDAR_10m_pmfgrd.spd -o LiDAR_1m_dsm.tif
```

### Create and View Virtual Raster Stack

```{sh}
# Create virtual raster stack
gdalbuildvrt -separate LiDAR_1m_dtm_dms_stack.vrt \
    LiDAR_1m_dtm.tif LiDAR_1m_dsm.tif
 
# Open composite in TuiView
tuiview --rgb -b 2,1,1 --stddev LiDAR_1m_dtm_dms_stack.vrt
```

### Create Hilshade

```{sh}
# Create Hilshade
gdaldem hillshade -of GTiff LiDAR_1m_dtm.tif \
LiDAR_1m_dtm_hillshade.tif
```


__1__ Zhang, K., Chen, S., Whitman, D., Shyu, M., Yan, J., Zhang, C., 2003. A progressive morphological filter for removing nonground measurements from airborne LIDAR data. IEEE Transactions on Geoscience and Remote Sensing 41 (4), pp. 872–882.

__2__ Evans, J. S., Hudak, A. T., 2007. A multiscale curvature algorithm for classifying discrete return lidar in forested environments. IEEE Transactions on Geoscience and Remote Sensing 45 (4), pp. 1029–1038.
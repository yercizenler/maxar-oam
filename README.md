# Scene Download

- Install dependencies
- Provide a scene id (catid) to the script to download
- The script will create a folder and download the tiles in it

# Merge

- Go to the scene directory
- Build VRT

```
gdalbuildvrt out.vrt *.tif
```

- Merge & Compress

```
gdal_translate out.vrt out.tif -a_nodata 0.0 -of GTiff -co BIGTIFF=YES -co TILED=YES -co COMPRESS=JPEG -co PHOTOMETRIC=YCBCR
```

# Rename & Upload to s3 bucket
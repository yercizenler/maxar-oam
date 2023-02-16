# Scene Download

- Install dependencies
- You need to have GDAL installed
- Provide credentials and a scene id (catid) to the script to download
- If you are on windows, you need to add `verify=False` to boto3.resource and requests
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

- Go to the scene directory and rename the out.tif
- Provide credentials and upload it to OAM S3 Bucket

- We are uploading files to `s3://hotosm-cdn/OAMimagery/` bucket
- You can reach them in as
`https://cdn.hotosm.org/OAMimagery/<name of file>`
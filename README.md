```
WARNING: The repo tries to automatize MAXAR image processing
before uploading to OAM on a local machine. The design and dependencies
are far away from a production-ready code.

contact: batuhankavlak4@gmail.com
```

The repository is designed to help HOT members to download, process, and upload MAXAR
open data in the Turkey & Syria Earthquake.

The current steps and stage is summarized as below:

- `download`: Searching `scene_id` through s3 maxar data bucket is used since there
isn't a STAC API hosting the data.
- `process`: For the sake of performance, GDAL commands are used to merge and compress data.
If not all the tiles are in the same projection, we are projecting them to `3857` and then mosaic.
- `upload`: A manual upload to OAM should be performed.

# Install Dependency

- Only supports Unix-like systems.
- Install GDAL to your local machine
- Install `requirements.txt` on python

# Set AWS Credentials

- Set the following environment keys as `.env` on vscode or to your bash
```
PERSONAL_AWS_KEY_ID=...
PERSONAL_AWS_SECRET=...
```

# Run the script

If you are brave to run all process:
```
python3 main.py --scene_id 10300500D9F8D500 --output_name "MAXAR_KAHRAMANMARAS.tif"
```

`main_multiscene_from_collection.py` is more practical for iterative processing.

# Uploading to OAM

- The image will be in the local file mosaiced.
- Use [OAM-UI](https://openaerialmap.org/) to upload.

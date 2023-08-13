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
- `upload`: The processed images are uploaded to HOT s3 bucket `"hotosm-cdn/OAMimagery"`.
Then a manual upload to OAM is performed.

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

`main_multiscene.py` is more practical for iterative processing.

If you wanna run only one part of the process, go to `manuals` and set variables manually. Then run.

# Uploading to OAM

- The image will be in `https://cdn.hotosm.org/OAMimagery/<name of file>`
- Use the link to upload to [OAM](https://openaerialmap.org/).
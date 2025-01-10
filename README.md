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
```shell
pip install -r requirements.txt
```

# Run the script

If you are brave to run all process:
```shell
python3 main.py --event_name  --scene_id 10300500D9F8D500 --output_name "MAXAR_KAHRAMANMARAS.tif"
```
You can find the latest event names downloading this [link](https://maxar-opendata.s3.amazonaws.com/events/catalog.json)

`main_multiscene_collection.py` is more practical for iterative processing if you download the collections.

Download collections:
```shell
aws s3 sync s3://maxar-opendata/events/{EVENT_NAME}/ard/acquisition_collections {REPO_PATH}/maxar-oam/data/{EVENT_NAME}/ --no-sign-request
```

Download items:
```shell
aws s3 cp s3://maxar-opendata/events/WildFires-LosAngeles-Jan-2025/ard/11/ {REPO_PATH}/maxar-oam/data/{EVENT_NAME}/items/temp --recursive --exclude "*" --include "*.json" --no-sign-request
```
Leaves single item per collection to check metadata:
```
find {REPO_PATH}/maxar-oam/data/{EVENT_NAME}/items/all -type f -name "*.json" -exec mv -f {} {REPO_PATH}/maxar-oam/data/{EVENT_NAME}/items/ \;
```

List bucket files:
```shell
aws s3 ls s3://maxar-opendata/events/{EVENT_NAME}/ard/ --no-sign-request
```

# Uploading to OAM

- The image will be in the local file mosaiced.
- Use [OAM-UI](https://openaerialmap.org/) to upload.

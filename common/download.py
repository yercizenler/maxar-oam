import requests
from pathlib import Path

import boto3

VERIFY=True # Set to False if you are on Windows

def download_tiles_s3(
        scene_id: str = "",
        download_path: Path = None,
        aws_access_key_id: str = "",
        aws_secret_access_key: str = ""
    ) -> None:
    s3 = boto3.resource(
            "s3",
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            verify=VERIFY
        )
    bucket = s3.Bucket(name="maxar-opendata")
    blobs = bucket.objects.filter(Prefix="")

    print("Detecting tiles")
    resource_list = [
        f"https://maxar-opendata.s3.amazonaws.com/{blob.key}" for blob in blobs if scene_id in blob.key
    ]
    tile_list = [url for url in resource_list if "visual" in url]

    for index, tile_url in enumerate(tile_list):
        print(f"downloading {tile_url}")
        r = requests.get(tile_url, allow_redirects=True, verify=VERIFY)
        with open(download_path / f'tile_{index}.tif', 'wb') as f:
            f.write(r.content)
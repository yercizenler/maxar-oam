import requests
from pathlib import Path

import boto3
import leafmap

def download_tiles_leafmap(
        scene_id: str = "",

):
    gdf = leafmap.maxar_items(
        collection_id='Kahramanmaras-turkey-earthquake-23',
        child_id=scene_id,
        return_gdf=True,
        assets=['visual']
    )
    image_list = gdf['visual'].tolist()

    Path(f"SCENES/{scene_id}").mkdir(parents=True, exist_ok=True)
    download_path = Path(f"SCENES/{scene_id}")  

    for index, tile_url in enumerate(image_list):
        print(f"downloading {tile_url}")
        r = requests.get(tile_url, allow_redirects=True)
        with open(download_path / f'tile_{index}.tif', 'wb') as f:
            f.write(r.content)


def download_tiles_s3(
        scene_id: str = "",
        aws_access_key_id: str = "",
        aws_secret_access_key: str = ""
    ) -> None:
    s3 = boto3.resource(
            "s3",
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
        )
    bucket = s3.Bucket(name="maxar-opendata")
    blobs = bucket.objects.filter(Prefix="")

    print("Detecting tiles")
    resource_list = [
        f"https://maxar-opendata.s3.amazonaws.com/{blob.key}" for blob in blobs if scene_id in blob.key
    ]
    tile_list = [url for url in resource_list if "visual" in url]

    Path(f"SCENES/{scene_id}").mkdir(parents=True, exist_ok=True)
    download_path = Path(f"SCENES/{scene_id}")  

    for index, tile_url in enumerate(tile_list):
        print(f"downloading {tile_url}")
        r = requests.get(tile_url, allow_redirects=True)
        with open(download_path / f'tile_{index}.tif', 'wb') as f:
            f.write(r.content)
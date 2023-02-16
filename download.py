import requests
from pathlib import Path

import boto3

scene_id = "10300100E18CB600"

s3 = boto3.resource(
        "s3",
        aws_access_key_id="AKIA47MNXXGLC7N6FZF4",
        aws_secret_access_key="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",
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

# Download tiles
for index, tile_url in enumerate(tile_list):
    print(f"downloading {tile_url}")
    r = requests.get(tile_url, allow_redirects=True)
    with open(download_path / f'tile_{index}.tif', 'wb') as f:
        f.write(r.content)
import os
from pathlib import Path

from common.download import download_tiles_s3

SCENE_ID = ""

Path(f"SCENES/{SCENE_ID}").mkdir(parents=True, exist_ok=True)
download_path = Path(f"SCENES/{SCENE_ID}")  

download_tiles_s3(
    scene_id=SCENE_ID,
    download_path=download_path,
    aws_access_key_id=os.environ["MAXAR_AWS_KEY_ID"],
    aws_secret_access_key=os.environ["MAXAR_AWS_SECRET"]
)
import os
from pathlib import Path

from common.download import download_tiles_s3
from common.upload import upload_scene

SCENE_ID = "10300100E131D000"
UPLOAD_PATH = Path(f"SCENES/SURIYE_AFRIN_20230212_MAXAR.tif")

download_tiles_s3(
    scene_id=SCENE_ID,
    aws_access_key_id=os.environ["HOT_AWS_KEY_ID"],
    aws_secret_access_key=os.environ["HOW_AWS_SECRET"]
)

upload_scene(
    upload_path=UPLOAD_PATH,
    aws_access_key_id=os.enviro["HOT_AWS_KEY_ID"],
    aws_secret_access_key=os.enviro["HOW_AWS_SECRET"]
)
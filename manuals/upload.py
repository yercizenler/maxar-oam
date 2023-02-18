import os
from pathlib import Path

from common.upload import upload_scene

OUTPUT_PATH = Path("")

upload_scene(
    upload_path=OUTPUT_PATH,
    aws_access_key_id=os.environ["MAXAR_AWS_KEY_ID"],
    aws_secret_access_key=os.environ["MAXAR_AWS_SECRET"]
)
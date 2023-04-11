import os
from pathlib import Path

import click

from common.download import download_tiles_s3
from common.process import process_scene
from common.upload import upload_scene

@click.command()
@click.option("--scene_id", default=None, help="CATID of the MAXAR scene.")
@click.option("--output_name", default="out.tif", help="Output TIFF name.")
def main(scene_id, output_name):

    Path(f"SCENES/{scene_id}").mkdir(parents=True, exist_ok=True)
    download_path = Path(f"SCENES/{scene_id}")  

    download_tiles_s3(
        scene_id=scene_id,
        download_path=download_path,
        aws_access_key_id=os.environ["PERSONAL_AWS_KEY_ID"],
        aws_secret_access_key=os.environ["PERSONAL_AWS_SECRET"]
    )

    output_path = Path(
        f"SCENES/{scene_id}/{output_name}"
    )

    process_scene(scene_path=download_path, output_path=output_path)

    upload_scene(
        upload_path=output_path,
        aws_access_key_id=os.environ["MAXAR_AWS_KEY_ID"],
        aws_secret_access_key=os.environ["MAXAR_AWS_SECRET"]
    )

if __name__ == '__main__':
    main()
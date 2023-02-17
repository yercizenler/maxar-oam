from pathlib import Path

import boto3

def upload_scene(
        upload_path: Path,
        aws_access_key_id: str,
        aws_secret_access_key: str
    ):
    """
    Uploads file to hotosm-cdn bucket to OAMimagery/
    """
    s3 = boto3.resource(
            "s3",
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
        )

    s3.meta.client.upload_file(
        upload_path, "hotosm-cdn", f"OAMimagery/{upload_path.name}"
    )
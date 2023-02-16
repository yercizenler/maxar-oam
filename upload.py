from pathlib import Path

import boto3

upload_path = Path("")

s3 = boto3.resource(
        "s3",
        aws_access_key_id="",
        aws_secret_access_key="",
    )

s3.meta.client.upload_file(upload_path, "hotosm-cdn", f"OAMimagery/{upload_path.name}")


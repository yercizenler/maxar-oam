from pathlib import Path
import os

from common.download import download_tiles_s3

LOCAL_INPUT_PATH = Path(__file__).parent.resolve().parent / "SCENES/"
TEST_SCENE_ID = "10300500D9F8D500"

Path(LOCAL_INPUT_PATH / TEST_SCENE_ID).mkdir(parents=True, exist_ok=True)

def test_download_tiles_s3_different_projection():
    download_tiles_s3(
            scene_id=TEST_SCENE_ID,
            download_path=LOCAL_INPUT_PATH / TEST_SCENE_ID,
            aws_access_key_id=os.environ["PERSONAL_AWS_KEY_ID"],
            aws_secret_access_key=os.environ["PERSONAL_AWS_SECRET"]
        )


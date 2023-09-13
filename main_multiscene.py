import os
from pathlib import Path
import pandas as pd
import requests

from common.download import download_tiles_s3
from common.process import process_scene
from common.upload import upload_scene

INPUT_DATA_PATH = Path(__file__).resolve().parent / "data/morocco_sep8.csv"

def main(csv_path: Path = INPUT_DATA_PATH):
    operation_df = pd.read_csv(csv_path)
    
    for index, row in operation_df.iterrows():
        if operation_df.at[index, "OperationState"] == "Finished":
            continue
        
        if operation_df.at[index, "OperationState"] == "NotStarted":
            operation_df.at[index, "OperationState"] = "Started"
            operation_df.to_csv(csv_path, index=False)
        
        scene_id = row["ImageId"]
        output_name = row["ImageName"]

        Path(f"SCENES/{scene_id}").mkdir(parents=True, exist_ok=True)
        download_path = Path(f"SCENES/{scene_id}")  

        if operation_df.at[index, "OperationState"] == "Started":
            download_tiles_s3(
                scene_id=scene_id,
                download_path=download_path,
                aws_access_key_id=os.environ["PERSONAL_AWS_KEY_ID"],
                aws_secret_access_key=os.environ["PERSONAL_AWS_SECRET"]
            )
            operation_df.at[index, "OperationState"] = "Downloaded"
            operation_df.to_csv(csv_path, index=False)

        output_path = Path(
            f"SCENES/{scene_id}/{output_name}"
        )

        if operation_df.at[index, "OperationState"] == "Downloaded":
            process_scene(scene_path=download_path, output_path=output_path)

            operation_df.at[index, "OperationState"] = "Processed"
            operation_df.to_csv(csv_path, index=False)

        #NOTE - Local manual upload is faster
        # if operation_df.at[index, "OperationState"] == "Processed":
        #     upload_scene(
        #         upload_path=output_path,
        #         aws_access_key_id=os.environ["MAXAR_AWS_KEY_ID"],
        #         aws_secret_access_key=os.environ["MAXAR_AWS_SECRET"]
        #     )

            operation_df.at[index, "OperationState"] = "Finished"
            operation_df.to_csv(csv_path, index=False)

if __name__ == '__main__':
    main()
import os
from pathlib import Path

import pandas as pd
import click

from common.download import download_tiles_from_dataset
from common.process import process_scene

@click.command()
@click.option("--operation_name", default="morocco_sep8", help="CATID of the MAXAR scene.")
def main(operation_name: str):
    metadata_path = Path(__file__).resolve().parent / f"data/{operation_name}_metadata.tsv"
    operation_table_path = Path(__file__).resolve().parent / f"data/{operation_name}.csv"
    
    metadata_df = pd.read_csv(metadata_path, sep="\t")
    operation_df = pd.read_csv(operation_table_path)
    
    for index, row in operation_df.iterrows():
        if operation_df.at[index, "OperationState"] == "Finished":
            continue
        
        if operation_df.at[index, "OperationState"] == "NotStarted":
            operation_df.at[index, "OperationState"] = "Started"
            operation_df.to_csv(operation_table_path, index=False, sep="\t")
        
        scene_id = row["ImageId"]

        metadata_df_filtered = metadata_df[metadata_df["catalog_id"] == scene_id]
        output_name = f"MERGED_{scene_id}.tif"

        Path(f"SCENES/{scene_id}").mkdir(parents=True, exist_ok=True)
        download_path = Path(f"SCENES/{scene_id}")  

        tile_list = list(metadata_df_filtered["visual"])
        if operation_df.at[index, "OperationState"] == "Started":
            download_tiles_from_dataset(
                download_path=download_path,
                tile_list=tile_list
            )
            operation_df.at[index, "OperationState"] = "Downloaded"
            operation_df.to_csv(operation_table_path, index=False, sep="\t")

        output_path = Path(
            f"SCENES/{scene_id}/{output_name}"
        )

        if operation_df.at[index, "OperationState"] == "Downloaded":
            process_scene(scene_path=download_path, output_path=output_path)

            operation_df.at[index, "OperationState"] = "Finished"
            operation_df.to_csv(operation_table_path, index=False, sep="\t")

if __name__ == '__main__':
    main()
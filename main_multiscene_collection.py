import pathlib

import json
import click

from common import download, process

@click.command()
@click.option("--operation_name", default="WildFires-LosAngeles-Jan-2025", help="Data folder path with scene collection jsons")
def main(operation_name: str):
    data_path = pathlib.Path(__file__).resolve().parent / f"data/{operation_name}"
    status_path = data_path / "operation_status.json"
    with status_path.open("r+") as sf:
        status_data = json.load(sf)
        for path in data_path.rglob("*collection.json"):
            with path.open("r") as cf:
                collection_json = json.load(cf)
                if not status_data.get(path.name):
                    status_data[path.name] = "Started"
                    sf.seek(0)
                    json.dump(status_data, sf, indent=4)
                
                download_path = pathlib.Path(f'SCENES/{collection_json["id"]}')
                download_path.mkdir(parents=True, exist_ok=True)
                if status_data[path.name] == "Started":
                    download_path = pathlib.Path(f'SCENES/{collection_json["id"]}')
                    download_path.mkdir(parents=True, exist_ok=True)
                    download.download_tiles_s3(
                        event_name=operation_name,
                        scene_id=collection_json["id"],
                        download_path=download_path,
                    )
                    status_data[path.name] = "Downloaded"
                    sf.seek(0)
                    json.dump(status_data, sf, indent=4) # save

                if status_data[path.name] == "Downloaded":
                    output_path = f'{download_path}/MERGED_{collection_json["id"]}.tif'
                    process.process_scene(
                        scene_path=download_path,
                        output_path=output_path
                    )
                    status_data[path.name] = "Finished"
                    sf.seek(0)
                    json.dump(status_data, sf, indent=4) # save

if __name__ == '__main__':
    main()
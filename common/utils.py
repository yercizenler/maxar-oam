from pathlib import Path
import json

import exifread

def is_projection_different(scene_path: Path) -> bool:
    file_list = scene_path.rglob("*tif")
    proj_list = [get_epsg_from_header(file_path) for file_path in file_list]

    return len(set(proj_list)) != 1

def get_epsg_from_header(file_path: Path) -> str:
    with file_path.open('rb') as f:
        header = exifread.process_file(f)

    for key in header.keys():
        if header.get(key).tag == 34737:
            return header.get(key).values
        
def write_and_update_dict(json_dict: dict, json_path: Path):
    with json_path.open("w") as f:
        json.dump(json_dict, f)
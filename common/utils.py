from pathlib import Path

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
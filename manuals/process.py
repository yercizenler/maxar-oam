from pathlib import Path

from common.process import process_scene

SCENE_FOLDER = Path("") # Only tif files with tiles are expected
OUTPUT_NAME = "" # with tif extension

output_path = SCENE_FOLDER / OUTPUT_NAME

process_scene(scene_path=Path(SCENE_FOLDER), output_path=output_path)

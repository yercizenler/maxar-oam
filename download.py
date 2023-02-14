import requests
from pathlib import Path

scene_id = "10300500D9F8CC00"
list_file = "aws_list.txt" # put it to the parent directory

Path(f"SCENES/{scene_id}").mkdir(parents=True, exist_ok=True)
download_path = Path(f"SCENES/{scene_id}")  

# Convert list
with open(list_file, "r") as aws_text:
    lines = aws_text.readlines()
    tile_list = []
    for l in lines:
        as_list = l.split(", ")
        tile_list.append(as_list[0])

    tile_list = [tile for tile in tile_list if scene_id in tile]
    clean_list = [tile.strip() for tile in tile_list]

# Download tiles
for index, tile_url in enumerate(clean_list):
    r = requests.get(tile_url, allow_redirects=True)
    with open(download_path / f'tile_{index}.tiff', 'wb') as f:
        f.write(r.content)
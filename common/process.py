from pathlib import Path
import subprocess
import os

from common.utils import is_projection_different

def process_scene(scene_path: Path, output_path: Path):
    """
    Process the image using GDAL commands.
    """
    if is_projection_different(scene_path=scene_path):
        project_to_3857(scene_path=scene_path)
        scene_path = scene_path / "PROJECTED"
    
    vrt_path = scene_path / "out.vrt"
    tif_pattern = scene_path / "*.tif"
    build_vrt(vrt_path=vrt_path, tif_pattern=tif_pattern)

    merge_and_compress_scene(
        vrt_path=vrt_path, output_path=output_path
    )

    pass

def project_to_3857(scene_path: Path):
    """
    Runs the below subprocess in a more pythonic way.

    gdalwarp
    """
    pass

def build_vrt(vrt_path: Path, tif_pattern: Path) -> None:
    """
    Runs the below subprocess in a more pythonic way.

    gdalbuildvrt out.vrt *.tif
    """
    
    cmd_list = ["gdalbuildvrt", str(vrt_path), str(tif_pattern)]
    os.system(subprocess.list2cmdline(cmd_list))
        
def merge_and_compress_scene(
        vrt_path: Path, output_path: Path
    ) -> None:
    """
    Runs the below subprocess in a more pythonic way.

    gdal_translate out.vrt out.tif \
        -a_nodata 0.0 -of GTiff -co BIGTIFF=YES -co TILED=YES \
        -co COMPRESS=JPEG -co PHOTOMETRIC=YCBCR
    """
    cmd_list = [
        "gdal_translate", f"{vrt_path}", f"{output_path}",
        "-a_nodata", "0.0", "-of", "GTiff",
        "-co", "BIGTIFF=YES", "-co", "TILED=YES",
        "-co", "COMPRESS=JPEG", "-co", "PHOTOMETRIC=YCBCR"
    ]

    os.system(subprocess.list2cmdline(cmd_list))
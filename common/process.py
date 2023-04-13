from pathlib import Path
import subprocess
import os

from common.utils import is_projection_different

def process_scene(scene_path: Path, output_path: Path):
    """
    Process the image using GDAL commands.
    """
    vrt_path = scene_path / "out.vrt"
    input_pattern = scene_path / "*.tif"

    if is_projection_different(scene_path=scene_path):
        projected_path = scene_path / "PROJECTED"
        projected_path.mkdir(parents=True, exist_ok=True)
        project_to_3857(
            scene_path=scene_path,
            projected_path=projected_path
        )

        scene_path = projected_path
        vrt_path = scene_path / "out.vrt"
        input_pattern = scene_path / "*.vrt"
    
    build_vrt(vrt_path=vrt_path, input_pattern=input_pattern)

    merge_and_compress_scene(
        vrt_path=vrt_path, output_path=output_path
    )

def project_to_3857(scene_path: Path, projected_path: Path):
    """
    Runs the below subprocess in a more pythonic way.

    gdalwarp -of VRT -srcnodata 0 input.tif output.vrt -t_srs EPSG:3857
    """
    for index, path in enumerate(scene_path.rglob("*tif")):
        out_vrt = str(projected_path / f"tile_{index}.vrt")
        cmd_list = [
            "gdalwarp", "-of", "VRT",
            "-srcnodata", "0.0",
            "-dstnodata", "0.0",
            str(path), out_vrt,
            "-t_srs", "EPSG:3857"
        ]
        os.system(subprocess.list2cmdline(cmd_list))


def build_vrt(vrt_path: Path, input_pattern: Path) -> None:
    """
    Runs the below subprocess in a more pythonic way.

    gdalbuildvrt out.vrt *.tif
    """
    
    cmd_list = [
        "gdalbuildvrt",
        "-srcnodata", "0.0",
        "-vrtnodata", "0.0",
        str(vrt_path), str(input_pattern)]
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
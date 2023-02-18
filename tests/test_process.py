"""
Simple tests for development purposes
"""

from pathlib import Path

from common.process import process_scene

LOCAL_INPUT_PATH = Path(__file__).parent.resolve().parent / "SCENES"

def test_process_scene_same_projection():
    process_scene(
        scene_path=LOCAL_INPUT_PATH / "TEST_SAME_PROJ",
        output_path=LOCAL_INPUT_PATH / "TEST_SAME_PROJ/test.tif"
    )

def test_process_scene_different_projection():
    process_scene(
        scene_path=LOCAL_INPUT_PATH / "TEST_DIFFERENT_PROJ",
        output_path=LOCAL_INPUT_PATH / "TEST_DIFFERENT_PROJ/test.tif"
    )
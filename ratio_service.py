import json
import re
from typing import List, Dict
from PIL import Image
from ratio_matcher import find_best_boards_for_image

CONFIG_PATH = "boards_config.json"

def get_image_ratio(image_path: str) -> float:
    with Image.open(image_path) as img:
        w, h = img.size
        return w / h

def parse_physical_dimensions(board_name: str):
    match = re.search(r"(\d+)x(\d+)(?!.*\d)", board_name)
    if match:
        return float(match.group(1)), float(match.group(2))
    return 1.0, 1.0

def load_boards_for_matcher():
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        config = json.load(f)
    
    boards_list = []
    for name in config.keys():
        phys_w, phys_h = parse_physical_dimensions(name)
        boards_list.append((name, phys_w, phys_h))
    return boards_list

def suggest_boards_for_image(img_path: str, max_diff: float = 0.3, top_k: int = 5):
    with Image.open(img_path) as img:
        w, h = img.size
    
    boards_metadata = load_boards_for_matcher()
    
    results = findbestboardsforimage(w, h, boards_metadata, maxdiff=max_diff)
    
    return results[:top_k]
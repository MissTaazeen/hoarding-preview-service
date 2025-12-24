import json
from PIL import Image
from ratio_service import suggest_boards_for_image

CONFIG_PATH = "boards_config.json"

with open(CONFIG_PATH, "r", encoding="utf-8") as f:
    BOARDS_CFG = json.load(f)

def place_creative_on_board(board_name: str, creative_path: str, output_path: str):
    cfg = BOARDS_CFG[board_name]
    
    board_img = Image.open(cfg["file"]).convert("RGB")
    creative_img = Image.open(creative_path).convert("RGB")
    
    creative_resized = creative_img.resize((cfg["w"], cfg["h"]))
    board_img.paste(creative_resized, (cfg["x"], cfg["y"]))
    
    board_img.save(output_path)
    return output_path

def generate_preview_for_image(creative_path: str, max_diff: float = 0.3):
    matches = suggest_boards_for_image(creative_path, max_diff=max_diff, top_k=1)
    
    if not matches:
        raise ValueError("No matching hoarding found for this image ratio.")
    
    best_match = matches[0]
    board_name = best_match["name"]
    
    output_path = "preview.png"
    place_creative_on_board(board_name, creative_path, output_path)
    
    return {
        "board": best_match,
        "preview_path": output_path
    }

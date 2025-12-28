import json
from typing import Dict

from PIL import Image

from ratio_service import suggest_boards_for_image

CONFIG_PATH = "boards_config.json"

with open(CONFIG_PATH, "r", encoding="utf-8") as f:
    BOARDS_CFG: Dict = json.load(f)


def _fit_creative_into_box(creative_img: Image.Image, box_w: int, box_h: int) -> Image.Image:
    cw, ch = creative_img.size

    if cw == 0 or ch == 0:
        raise ValueError("Creative image has invalid dimensions.")

    scale = min(box_w / cw, box_h / ch)
    new_w = max(1, int(cw * scale))
    new_h = max(1, int(ch * scale))

    return creative_img.resize((new_w, new_h), Image.Resampling.LANCZOS)


def place_creative_on_board(board_name: str, creative_path: str, output_path: str) -> str:
    cfg = BOARDS_CFG[board_name]

    board_img = Image.open(cfg["file"]).convert("RGB")
    creative_img = Image.open(creative_path).convert("RGB")

    x = int(cfg["x"])
    y = int(cfg["y"])
    box_w = int(cfg["w"])
    box_h = int(cfg["h"])

    creative_resized = _fit_creative_into_box(creative_img, box_w, box_h)

    rw, rh = creative_resized.size
    paste_x = x + (box_w - rw) // 2
    paste_y = y + (box_h - rh) // 2

    board_img.paste(creative_resized, (paste_x, paste_y))

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
        "preview_path": output_path,
    }

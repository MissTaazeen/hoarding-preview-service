import json
from PIL import Image
from ratio_service import suggest_boards_for_image

CONFIG_PATH = "boards_config.json"

# Load board overlay configuration once
with open(CONFIG_PATH, "r", encoding="utf-8") as f:
    BOARDS_CFG = json.load(f)


def place_creative_on_board(board_name: str, creative_path: str, output_path: str) -> str:
    
    if board_name not in BOARDS_CFG:
        raise ValueError(f"No config for board '{board_name}'")

    cfg = BOARDS_CFG[board_name]
    board_file = cfg["file"]
    x, y, w, h = cfg["x"], cfg["y"], cfg["w"], cfg["h"]

    board_img = Image.open(board_file).convert("RGB")
    creative_img = Image.open(creative_path).convert("RGB")

    # resize creative to fit board area
    creative_resized = creative_img.resize((w, h))

    # paste onto board at (x, y)
    board_img.paste(creative_resized, (x, y))

    board_img.save(output_path)
    return output_path


def generate_preview_for_image(
    creative_path: str,
    max_diff: float = 0.3,
    top_k: int = 1,
    output_path: str = "preview.png",
) -> dict:
    matches = suggest_boards_for_image(creative_path, max_diff=max_diff, top_k=top_k)
    if not matches:
        raise ValueError("No boards configured")

    best = matches[0]
    board_name = best["name"]

    place_creative_on_board(board_name, creative_path, output_path)

    return {
        "board": best,
        "preview_path": output_path,
    }
